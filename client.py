import rpyc
import sys

if len(sys.argv) < 2:
    exit("Usage {} IP_DO_SERVIDOR".format(sys.argv[0]))

server = sys.argv[1]

conn = rpyc.connect(server, port=18861)

print(conn.root)
print(conn.root.get_answer())
print(conn.root.the_real_answer_though)