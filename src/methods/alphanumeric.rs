use crate::constants::ALPHANUMERIC;
use pyo3::prelude::*;
use rand::{distributions::Alphanumeric, Rng};

#[pyfunction]
pub fn alphanumeric(length: usize, prefix: &str) -> String {
    println!("The constant value {}", ALPHANUMERIC);
    let generated: String = rand::thread_rng()
        .sample_iter(&Alphanumeric)
        .take(length)
        .map(char::from)
        .collect();

    if prefix.is_empty() {
        return generated;
    }

    return prefix.to_string() + &generated;
}
