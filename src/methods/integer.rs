use rand::Rng;

pub fn integer() -> u8 {
    let mut rng = rand::thread_rng();

    let generated: u8 = rng.gen();

    return generated;
}
