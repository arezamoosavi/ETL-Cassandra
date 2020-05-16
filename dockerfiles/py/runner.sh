#!/bin/bash
#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


function cassandra_ready(){
python << END
try:
    print('\n'*5,'Connecting to Cassandra . . .', '\n'*5)
    exit(1)
except:
    exit(0)
END
}

until cassandra_ready; do
    >&2 echo "Waiting Cassandra Service..."
    sleep 1
done
echo "Cassandra is Ready.. Let's go!"

echo "print('Runner')" | python

while python connect.py; do echo 'sleeping...'; sleep 5; done;

# python connect.py

echo "Done! . . . . ."


exec "$@"