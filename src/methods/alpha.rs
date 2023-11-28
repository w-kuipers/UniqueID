use crate::constants::{ALPHA, ALPHA_LOWER, ALPHA_UPPER};
use pyo3::prelude::*;
use rand::Rng;

#[pyfunction]
pub fn alpha(length: usize, prefix: &str, case: &str) -> String {
    let mut rng = rand::thread_rng();

    let charset: &[u8] = match case {
        "upper" => ALPHA_UPPER,
        "lower" => ALPHA_LOWER,
        _ => ALPHA,
    };

    let generated: String = (0..length)
        .map(|_| {
            let idx = rng.gen_range(0..charset.len());
            charset[idx] as char
        })
        .collect();

    if prefix.is_empty() {
        return generated;
    }

    return prefix.to_string() + &generated;
}
