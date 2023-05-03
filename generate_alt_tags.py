from storage_service import StorageService
from recognition_service import RecognitionService

storage_service = StorageService()
recognition_service = RecognitionService()

bucket_name = '>>YOUR.S3.BUCKET.NAME.HERE<<'

for file in storage_service.get_all_files(bucket_name):
    if file.key.endswith('.jpg'):
        print('Image: ' + file.key)
        labels = recognition_service.detect_objects(file.bucket_name, file.key)

        print("Alt tags for this image: ")
        for label in labels:
            print(label['Name'])
        print()  # Add newline