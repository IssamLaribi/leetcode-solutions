class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()  # FIFO packets
        self.seen = set()  # track duplicates
        self.dest_map = defaultdict(list)  # dest -> sorted timestamps

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.seen:
            return False

        # evict if full
        if len(self.queue) == self.memoryLimit:
            old_src, old_dst, old_ts = self.queue.popleft()
            self.seen.remove((old_src, old_dst, old_ts))
            idx = bisect.bisect_left(self.dest_map[old_dst], old_ts)
            if idx < len(self.dest_map[old_dst]) and self.dest_map[old_dst][idx] == old_ts:
                self.dest_map[old_dst].pop(idx)

        # add new packet
        self.queue.append((source, destination, timestamp))
        self.seen.add(key)
        self.dest_map[destination].append(timestamp)  # timestamps increasing
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        src, dst, ts = self.queue.popleft()
        self.seen.remove((src, dst, ts))
        idx = bisect.bisect_left(self.dest_map[dst], ts)
        if idx < len(self.dest_map[dst]) and self.dest_map[dst][idx] == ts:
            self.dest_map[dst].pop(idx)
        return [src, dst, ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        times = self.dest_map[destination]
        left = bisect.bisect_left(times, startTime)
        right = bisect.bisect_right(times, endTime)
        return right - left
