use pyo3::prelude::*;
use rand::Rng;

enum Case {
    All,
    Upper,
    Lower,
}

#[pyfunction]
pub fn alpha(length: usize, prefix: &str, case: &Case) -> String {
    const CHARSET: &[u8] = b"abcdefghijklmnopABCDEFGHIJKLMNOP";
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
