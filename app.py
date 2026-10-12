from tasks import add_task, complete_task, list_tasks

if __name__ == "__main__":
    add_task("Write report", "high")
    add_task("Buy milk")
    complete_task(0)
    for t in list_tasks():
        print(t)
