#!/bin/bash
#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


function cassandra_ready(){
python << END
import sys

try:
    print('\n'*5,'Connecting to Cassandra . . .', '\n'*5)
    sys.exit(0)
except:
    print('\n'*5,'Error In Connection . . .', '\n'*5)
    sys.exit(-1)
finally:
    raise SystemExit(1)
END
}

echo "Waiting Cassandra Service..."
sleep 1

cassandra_ready

echo "Cassandra is Ready.. Let's go!"

echo "print('built')" | python


exec "$@"

exit 0