import os

target_files = [
    '/dbc/permanent/brazil_kits.dbc',
    '/dbc/permanent/forbidden names.dbc',
    '/dbc/permanent/Licensing2.dbc',
    '/dbc/permanent/Licensing2_chn.dbc',
    '/dbc/permanent/zebra award.dbc',
    '/dbc/permanent/zebra turin fake staff.dbc',
    '/edt/permanent/fake.edt',
    '/lnc/all/fake.lnc',
    '/lnc/all/lic_dan_swe_fra.lnc',
    '/lnc/all/nleague.lnc',
    '/lnc/temporary/names.lnc',
    '/lnc/temporary/zebre.lnc',
]
fm_base_data = os.path.abspath('../../Library/Application Support/Steam/steamapps/common/Football Manager '
                               '2021/data/database/db')

license_folders = os.listdir(fm_base_data)[1:]

for update_folder in license_folders:
    for file in target_files:
        file_path = f'{fm_base_data}/{update_folder}{file}'
        try:
            os.remove(file_path)
            print(f'File {file_path} removed!')
        except FileNotFoundError:
            print(f"{file_path} - File doesn't exists'\n")
