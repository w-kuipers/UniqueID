use rand::{distributions::Alphanumeric, Rng};

pub fn alphanumeric(length: usize, prefix: &str) -> String {
    let generated: String = rand::thread_rng()
        .sample_iter(&Alphanumeric)
        .take(length)
        .map(char::from)
        .collect();

    if prefix.is_empty() {
        println!("no prefix");
        return generated;
    }

    return prefix.to_string() + &generated;
}
