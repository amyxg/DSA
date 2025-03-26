"""
program constructs a bounded queue with a limit of 4 items and an unbounded queue. 
Then eight calls to each queue's enqueue() method occur, followed by two dequeue() calls, 
then four more enqueue() calls. Then each queue's contents are displayed.

@amyxg

"""
from ArrayQueue import ArrayQueue

# Make two queues, one bounded to 4 items and the other bounded
boundedQueue = ArrayQueue(4)
unboundedQueue = ArrayQueue()
        
# Enqueue 8 items in each
print("Enqueueing values 1 through 8 to each queue")
for i in range(1, 9):
    boundedQueue.enqueue(i)
    unboundedQueue.enqueue(i)
       
# Dequeue two items from each queue
print("Dequeuing twice")
for i in range(2):
    print(f"  Dequeued {boundedQueue.dequeue()}", end="")
    print(" from bounded queue");
    print(f"  Dequeued {unboundedQueue.dequeue()}", end="")
    print(" from unbounded queue")

# Enqueue 4 more items
print("Enqueueing values: 10, 20, 30 and 40")
for i in [10, 20, 30, 40]:
    boundedQueue.enqueue(i)
    unboundedQueue.enqueue(i)
        
# Display contents of each queue
print("Bounded queue (maxLength=", end="")
print(f"{boundedQueue.get_max_length()}", end="")
print(") contents:")
while boundedQueue.get_length() > 0:
    print(f"  {boundedQueue.dequeue()}")
print("Unbounded queue contents:")
while unboundedQueue.get_length() > 0:
    print(f"  {unboundedQueue.dequeue()}")