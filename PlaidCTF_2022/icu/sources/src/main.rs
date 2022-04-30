use img_hash::image;
use img_hash::HasherConfig;

mod secret;
use crate::secret::{FLAG, FLAG_TOO};

fn bindiff_of_1(fn1: &str, fn2: &str) -> bool {
    use std::io::Read;
    let b1: Vec<u8> = std::fs::File::open(fn1)
        .unwrap()
        .bytes()
        .collect::<Result<_, _>>()
        .unwrap();
    let b2: Vec<u8> = std::fs::File::open(fn2)
        .unwrap()
        .bytes()
        .collect::<Result<_, _>>()
        .unwrap();
    if b1.len() != b2.len() {
        return false;
    }
    b1.into_iter()
        .zip(b2.into_iter())
        .map(|(x, y)| (x ^ y).count_ones())
        .sum::<u32>()
        == 1
}

fn main() {
    let args = std::env::args().collect::<Vec<_>>();

    let (fn1, fn2) = if args.len() == 1 {
        use rand::Rng;
        use std::io::Write;
        let now = chrono::offset::Local::now();
        let dir = format!("{}", now.format("images/%Y-%m-%d-%H"));
        let prefix = format!(
            "{}/{}-{}",
            dir,
            now.format("%Y-%m-%d-%H%M%S"),
            (0..5)
                .map(|_| rand::thread_rng().gen_range('A'..='Z'))
                .collect::<String>(),
        );
        let b1 = {
            println!("Image 1 (base64):");
            let mut s: String = String::new();
            std::io::stdin().read_line(&mut s).unwrap();
            if s.len() > 200_000 {
                println!("Too big");
                std::process::exit(2);
            }
            base64::decode(s.trim()).unwrap()
        };
        let b2 = {
            println!("Image 2 (base64):");
            let mut s: String = String::new();
            std::io::stdin().read_line(&mut s).unwrap();
            if s.len() > 200_000 {
                println!("Too big");
                std::process::exit(2);
            }
            base64::decode(s.trim()).unwrap()
        };
        std::fs::create_dir_all(dir).unwrap();
        let suffix = {
            if b1[0..4] == b2[0..4] && b1[0..4] == [0x89, 0x50, 0x4e, 0x47] {
                "png"
            } else if b1[6..10] == b2[6..10] && b1[6..10] == [0x4a, 0x46, 0x49, 0x46] {
                "jpg"
            } else {
                println!("Unknown formats");
                std::process::exit(3);
            }
        };
        let fn1 = format!("{}-img1.{}", prefix, suffix);
        let fn2 = format!("{}-img2.{}", prefix, suffix);
        std::fs::File::create(&fn1).unwrap().write_all(&b1).unwrap();
        std::fs::File::create(&fn2).unwrap().write_all(&b2).unwrap();
        (fn1, fn2)
    } else if args.len() == 3 {
        (args[1].clone(), args[2].clone())
    } else {
        eprintln!("Usage: {} [img1.png img2.png]", args[0]);
        std::process::exit(1);
    };

    let image1 = image::open(&fn1).unwrap();
    let image2 = image::open(&fn2).unwrap();

    let hasher = HasherConfig::new().to_hasher();

    let hash1 = hasher.hash_image(&image1);
    let hash2 = hasher.hash_image(&image2);
    

    println!("Image1 hash: {}", hash1.to_base64());
    println!("Image2 hash: {}", hash2.to_base64());

    let dist = hash1.dist(&hash2);
    println!("Hamming Distance: {}", dist);

    let text1 = tesseract::ocr(&fn1, "eng")
        .unwrap()
        .trim()
        .split_whitespace()
        .collect::<Vec<_>>()
        .join(" ");
    let text2 = tesseract::ocr(&fn2, "eng")
        .unwrap()
        .trim()
        .split_whitespace()
        .collect::<Vec<_>>()
        .join(" ");

    println!("Image 1 text: {}", text1);
    println!("Image 2 text: {}", text2);

    if dist == 0
        && text1.to_lowercase() == "sudo please"
        && text2.to_lowercase() == "give me the flag"
        && hash1.to_base64() == "ERsrE6nTHhI="
    {
        println!("Congratulations: {}", FLAG);
    } else if dist > 0
        && text1.to_lowercase() == "give me the flag"
        && text2.to_lowercase() == "give me the flag"
        && bindiff_of_1(&fn1, &fn2)
    {
        println!("Wow, impressive: {}", FLAG_TOO);
    } else {
        println!("Try again");
    }
}
