use pyo3::prelude::*;
use rand::Rng;

#[pyfunction]
pub fn numeric(length: usize, prefix: &str) -> String {
    const CHARSET: &[u8] = b"0123456789";
    let mut rng = rand::thread_rng();

    let generated: String = (0..length)
        .map(|_| {
            let idx = rng.gen_range(0..CHARSET.len());
            CHARSET[idx] as char
        })
        .collect();

    if prefix.is_empty() {
        return generated;
    }

    return prefix.to_string() + &generated;
}
