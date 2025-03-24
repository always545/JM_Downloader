import jmcomic
config = jmcomic.create_option_by_file('../config/jmconfig.yml')
jm_code = 'JM121021'
jmcomic.download_album(jm_code,config)