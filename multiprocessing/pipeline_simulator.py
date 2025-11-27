# simulating a raw serial pipeline (no async)

from multiprocessing import Process, Queue, cpu_count, Semaphore, Manager, freeze_support, set_start_method

def producer(q, num, name, sem):
    with sem:
        q.put(num)
        print(f"{name} took {num} from jobs list and put it in produced_num_queue.")
    return

def processor(input_queue, output_queue, name, sem):
    with sem:
        num = input_queue.get()
        result_num = num ** 3
        output_queue.put(result_num)
        print(f"{name} cubed {num} -> {result_num} and put it in the processed_num_queue")
    return

if __name__ == '__main__':

    freeze_support()

    manager = Manager()
    sem = manager.Semaphore(cpu_count() // 4)

    jobs = [12, 45, 67, 23, 89, 34, 56, 78, 90, 11, 29, 64, 38, 72, 55, 81, 93, 47, 19, 68]
    
    produced_num_queue = Queue()
    processed_num_queue = Queue()

    print(jobs)
    print(sem, cpu_count())

    processes = [Process(target=producer, args=(produced_num_queue, job, f"{i}th producer process", sem)) for i, job in enumerate(jobs)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    
    processes = []
    for i in range(len(jobs)):
        processes.append(Process(target=processor, args=(produced_num_queue, processed_num_queue, f"{i}th processor process", sem)))
    for process in processes:
        process.start()
    for process in processes:
        process.join()

    results = []
    while not processed_num_queue.empty():
        results.append(processed_num_queue.get())
    print(results)