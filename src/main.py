from apache_beam.options.pipeline_options import PipelineOptions
from lib.test_app import test_app


if __name__ == "__main__":
    import argparse
    import logging

    logging.getLogger().setLevel(logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-text",
        default="default input text",
        help="input text to print",
    )
    args, beam_args = parser.parse_known_args()
    beam_options = PipelineOptions(
        save_main_session=True,
        setup_file="./setup/setup.py"
    )
    test_app.run(
        input_text=args.input_text, 
        beam_option=beam_options,
    )

