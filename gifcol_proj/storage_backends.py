from storages.backends.s3boto3 import S3Boto3Storage
# куда загружаем файлы на S3 Amazon
class MediaStorage(S3Boto3Storage):
    location = 'media/file'
    file_overwrite = False