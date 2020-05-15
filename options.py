import pathlib,os
test_run = False
if not pathlib.Path(pathlib.Path(__file__).parent).joinpath('data').exists():
    os.mkdir(str(pathlib.Path(pathlib.Path(__file__).parent).joinpath('data')))

data_path = str(pathlib.Path(pathlib.Path(__file__).parent).joinpath('data')) if not test_run else str(pathlib.Path(pathlib.Path(__file__).parent).joinpath('test_data'))

if not pathlib.Path(pathlib.Path(__file__).parent).joinpath('log').exists():
    os.mkdir(str(pathlib.Path(pathlib.Path(__file__).parent).joinpath('log')))
    log_path = str(pathlib.Path(pathlib.Path(__file__).parent).joinpath('log').joinpath('log.log'))
else:
    log_path = str(pathlib.Path(pathlib.Path(__file__).parent).joinpath('log').joinpath('log.log'))