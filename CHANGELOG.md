# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Added exception that will raise when specified length is higher than 100000 if "ignore_max_length" argument is set to False.

### Removed
- Removed unnecessary imports.

## [v0.1.4] - 2022-02-17
### Fixed
- Issue where "integer" function will not be accurate when the randomly generated integer started with 0.
- Issue where "integer" and "string" functions would fail when no "prefix" was specified.

### Documentation
- Added information for "database" function.

[0.1.4]: https://github.com/w-kuipers/simpleUID/compare/v0.1.3...v0.1.4
[0.0.1]: https://github.com/w-kuipers/simpleUID/releases/tag/v0.0.1