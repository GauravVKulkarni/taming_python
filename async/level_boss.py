# simulation of a pipeline (producer -> processor -> consumer)

import asyncio
import random



async def producer(vid_data_obj, processing_queue):
    # This function takes a video metadata object and adds it to the queue affter a delay to simulate real time video uploads
    # input format - vid_data_obj : {object} {"id" : str, "filename" : str, "size_mb" : int, "uploader" : str}, processing_queue : {queue}
    await asyncio.sleep(random.randint(0,3))
    await processing_queue.put(vid_data_obj)
    print(f'{vid_data_obj["id"]} uploaded. entered into the processing queue.')



async def processor(processing_queue, consumer_queue):
    
    # This function takes a queue containing video metadata objects, processes them asynchronously and puts the processed data in the consumer_queue
    # input format - processing_queue : {queue}, consumer_queue : {queue}

    # object mapping the codec to its bitrate value (mbps)
    bitrate_map = {
        ".mp4": 3,
        ".mov": 6,
        ".mkv": 4,
    }

    # an indefinitely running processor loop that processes tasks taken from processor queue and accepts the next task from the queue as soon as it is available
    while True:
        obj = await processing_queue.get()
        try:
            print(f'started processing {obj["id"]}....')
            await asyncio.sleep(random.randint(2,4))
            processed_obj = {}
            processed_obj["id"] = obj["id"]
            processed_obj["codec"] = f'.{obj["filename"].split(".")[1].lower()}'
            processed_obj["duration"] = obj["size_mb"] // bitrate_map[processed_obj["codec"]]

            await consumer_queue.put(processed_obj)
            print(f'Finished processing {obj["id"]}. entered into the consumer queue.')
        except:
            print(f'failed processing {obj["id"]}')
        finally:
            processing_queue.task_done()



async def consumer(consumer_queue, db_aka_list):
    # This function takes processed objects from the consumer queue and stores them in a list with a delay, mimicking database transaction.
    # input format - consumer_queue : {queue}, db_aka_list : {list}

    # an indefinitely running consumer loop that sends objects in consumer queue to storage as soon as it is available
    while True:
        obj = await consumer_queue.get()
        try:
            print(f'Started storing {obj["id"]}....')
            await asyncio.sleep(random.randint(3,6))
            db_aka_list.append(obj)
            print(f'Stored {obj["id"]}.')
        finally:
            consumer_queue.task_done()



async def orchestrator(sample_videos):

    # the function that handles the components of the pipeline

    processing_queue = asyncio.Queue()
    consumer_queue = asyncio.Queue()

    db_aka_list = []

    # spawn tasks
    producers = [asyncio.create_task(producer(obj, processing_queue)) for obj in sample_videos]
    processors = [asyncio.create_task(processor(processing_queue, consumer_queue)) for _ in range(2)]
    consumers = [asyncio.create_task(consumer(consumer_queue, db_aka_list)) for _ in range(1)]

    # wait until queues are done
    await asyncio.gather(*producers)
    await processing_queue.join()
    await consumer_queue.join()

    # optionally cancel background processors/consumers
    for p in processors + consumers:
        p.cancel()
    
    return db_aka_list


if __name__ == '__main__':

    sample_videos = [
        {"id": "vid_001", "filename": "travel_vlog.mp4",      "size_mb": 120, "uploader": "userA"},
        {"id": "vid_002", "filename": "cooking_show.mov",     "size_mb": 450, "uploader": "chefX"},
        {"id": "vid_003", "filename": "gaming_clip.mkv",      "size_mb": 60,  "uploader": "proGamer"},
        {"id": "vid_004", "filename": "wedding_highlights.mp4","size_mb": 980, "uploader": "studio99"},
        {"id": "vid_005", "filename": "documentary.mov",       "size_mb": 210, "uploader": "filmNerd"},
        {"id": "vid_006", "filename": "drone_shot.mp4",        "size_mb": 700, "uploader": "pilotZ"},
        {"id": "vid_007", "filename": "cat_video.mp4",         "size_mb": 12,  "uploader": "petOwner"},
        {"id": "vid_008", "filename": "music_video.mkv",       "size_mb": 330, "uploader": "bandY"},
        {"id": "vid_009", "filename": "interview.mov",         "size_mb": 240, "uploader": "journalist"},
        {"id": "vid_010", "filename": "tutorial.mp4",          "size_mb": 100, "uploader": "teacher101"},
    ]

    print("Starting the pipeline....")
    print(asyncio.run(orchestrator(sample_videos)))