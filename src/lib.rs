use pyo3::prelude::*;
mod methods;

/// A Python module implemented in Rust.
#[pymodule]
fn simpleuid(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(methods::alphanumeric::alphanumeric, m)?)?;
    m.add_function(wrap_pyfunction!(methods::numeric::numeric, m)?)?;
    Ok(())
}
