# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Basic library test"""

# imports: library
import json
from types import ModuleType

# imports: testing
import basic_1
import basic_2
import basic_3

# imports: project
import libmonty_logging
import libmonty_logging.configs
import libmonty_logging.paths
import libmonty_logging.version

MOCK_PROGRAM_NAME = libmonty_logging.version.PROGRAM_NAME + '-test'
MOCK_PROGRAM_VERSION = libmonty_logging.version.__version__


def line_display_format(line: str) -> str:
    """Create a display format of a config line for comparison"""

    return (
        line
        .replace(' ', '·')
        .replace('\t', '↹')
        .replace('\r', '⤶')
        .replace('\n', '⤶')
    )


def test(module: ModuleType) -> None:
    """Test"""

    reference, config = module.create_config(
        program_name=MOCK_PROGRAM_NAME,
        program_version=MOCK_PROGRAM_VERSION
    )

    libmonty_logging.apply_config(config)

    generated: str = json.dumps(config, indent=2)

    if not generated == reference:
        print()
        print(f'{"  REFERENCE  ":-^80}')
        print()
        print(reference)

        print()
        print(f'{"  GENERATED  ":-^80}')
        print()
        print(generated)

        print()
        print(f'{"  DIFFERENCE  ":-^80}')

        reference_lines: list[str] = reference.split('\n')
        generated_lines: list[str] = generated.split('\n')

        for i_line, ref_and_gen in enumerate(zip(reference_lines, generated_lines)):
            line_ref, line_gen = ref_and_gen
            if line_ref != line_gen:
                print()
                print('Line', i_line)
                print('REF:', line_display_format(line_ref))
                print('GEN:', line_display_format(line_gen))

    print()
    print(f'{"  RESULT  ":-^80}')
    print()
    if generated == reference:
        print('Generated and reference versions are equal')
    else:
        print('PROBLEM: Generated and reference versions are NOT equal')


def main() -> None:
    """Main"""

    total_tests: int = 3

    def header_text(current_test: int) -> str:
        """Header text for display"""
        return '  ' + f'{current_test}/{total_tests}' + '  '

    print()
    print(f'{header_text(1):=^80}')
    test(basic_1)

    print()
    print(f'{header_text(2):=^80}')
    test(basic_2)

    print()
    print(f'{header_text(3):=^80}')
    test(basic_3)

    print()
    print(f'{"":=^80}')


if __name__ == '__main__':
    main()
