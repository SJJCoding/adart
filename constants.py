ADQ_WORKING_FOLDER = ".adq"
PROJECTS = "projects"
TASKS = "tasks"
JSON_EXT = ".json"
CHARTS = "charts"

CVAT_XML = "CVAT XML"
PASCAL_VOC_XML = "PASCAL VOC XML"
COCO_JSON = "COCO JSON"
ADQ_JSON = "ADQ JSON"

SUPPORTED_FORMATS = [CVAT_XML, PASCAL_VOC_XML, COCO_JSON, ADQ_JSON]
SUPPORTED_IMAGE_FILE_EXTENSIONS = "*.jpg *.jpeg *.png *.bmp *.tiff *.gif"
SUPPORTED_VIDEO_FILE_EXTENSIONS = "*.mp4 *.avi *.mov"
SUPPORTED_AUDIO_FILE_EXTENSIONS = "*.mp3 *.wav"

PROJECT_COLUMNS = ['id', 'name', 'file_format_id',
                   'total_count', 'task_total_count', 'task_done_count']

TASK_COLUMNS = ['id', 'name', "project_id"]