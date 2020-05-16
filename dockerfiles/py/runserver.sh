#!/bin/bash
#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


function cassandra_ready(){
python << END
print('\n'*5,'Connecting to Cassandra . . .', '\n'*5)
END
}

echo "Waiting Cassandra Service..."
sleep 1

cassandra_ready

echo "Cassandra is Ready.. Let's go!"

echo "print('built')" | python

python db/printt.py

sleep 50

python project.py

echo "Done! . . . . ."


exec "$@"

exit 0