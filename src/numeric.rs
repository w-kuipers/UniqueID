use rand::{distributions::Alphanumeric, Rng};

pub fn numerical(length: usize) -> String {
    let generated: String = rand::thread_rng()
        .sample_iter(&Alphanumeric)
        .take(length)
        .map(char::from)
        .collect();

    return generated;
}
