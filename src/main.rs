mod alphanumeric;

fn main() {
    let generated: String = alphanumeric::alphanumeric(30090, "");

    println!("{}", generated);
}
