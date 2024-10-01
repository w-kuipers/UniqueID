# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [unreleased]

### Changed

- Improve parameter types
- Add documentation to functions

## [1.1.2]

### Changed

- Change set of symbols included in method "password".

## [1.1.1]

### Changed

- "password" method now adds symbols by default. This can be disabled by setting the "symbols" parameter to False.

## [1.1.0] - 2023-11-28

### Added

- `MongoDB` support for `database` method.

## [1.0.0]

### Fixed

= Cleaned up code for release.

## [1.0.0-alpha.3]

### Fixed

- "var" methods were not behaving the way they should.

### Added

- Short versions of date variables to "var" method.

## [1.0.0-alpha.2]

### Changed

- "var" method in database will now add up until it's unique.

## [1.0.0-alpha]

### Added

- "var" function to generate a string based on a variable string that is passed as an argument.
- "var" method to "database" function.

### Changed

- Changed 'default_max_length' to 1000.

### Removed

- Removed "secret" function as it was depricated.
- Removed deprication warning when "string" function was given type "integer" instead of "numbers".

## [0.1.6] - 2022-03-08

### Added

- Arguments "lowercase_only" and "uppercase_only" to the "string" function.
- "string" function argument "type" will now take "all". It will then return a string containing both numbers and letters.

### Changed

- "string" function argument "type" will take "numbers" instead of "integer". This is deprecated in this version and will be removed in version 1.0.0.
- "secret" function split up into seperate "bytes", "hex" and urlsafe functions. This is deprecated in this version and will be removed in version 1.0.0.

### Removed

- Removed "colorama" dependency as it was unnecessary.

## [0.1.5] - 2022-02-27

### Fixed

- Issue where "database" function would fail if argument "method" was undefined.
- Issue where "integer" function failed because a variable was defined out of scope.

### Added

- Added exception that will raise when specified length is higher than 100000 if "ignore_max_length" argument is set to False.
- Added "type" argument to "string" function. This adds the option to create a string of numbers.

### Removed

- Removed unnecessary imports.
- Removed unnecessary code.

### Documentation

- Added information for "secret" function.

## [0.1.4] - 2022-02-17

### Fixed

- Issue where "integer" function will not be accurate when the randomly generated integer started with 0.
- Issue where "integer" and "string" functions would fail when no "prefix" was specified.

### Documentation

- Added information for "database" function.

[unreleased]: https://github.com/w-kuipers/simpleUID/compare/v1.1.2...HEAD
[1.1.2]: https://github.com/w-kuipers/simpleUID/compare/v1.1.1...v1.1.2
[1.1.1]: https://github.com/w-kuipers/simpleUID/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/w-kuipers/simpleUID/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/w-kuipers/simpleUID/compare/v0.1.6...v1.0.0
[1.0.0-alpha.3]: https://github.com/w-kuipers/simpleUID/compare/v0.1.6...v1.0.0-alpha.3
[1.0.0-alpha.2]: https://github.com/w-kuipers/simpleUID/compare/v0.1.6...v1.0.0-alpha.2
[1.0.0-alpha]: https://github.com/w-kuipers/simpleUID/compare/v0.1.6...v1.0.0-alpha
[0.1.6]: https://github.com/w-kuipers/simpleUID/compare/v0.1.5...v0.1.6
[0.1.5]: https://github.com/w-kuipers/simpleUID/compare/v0.1.4...v0.1.5
[0.1.4]: https://github.com/w-kuipers/simpleUID/compare/v0.1.3...v0.1.4
[0.0.1]: https://github.com/w-kuipers/simpleUID/releases/tag/v0.0.1
