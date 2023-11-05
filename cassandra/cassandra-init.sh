#!/usr/bin/env bash

until printf ""2>>/dev/null >>/dev/tcp/cassandra/9042; do
    sleep 5;
    echo "Waiting for cassandra...";
done

echo "Creating keyspace and table..."
csql cassandra -u cassandra -p cassandra -e "CREATE KEYSPACE IF NOT EXISTS order_ks WITH replication = {'class':'SimpleStrattegy', 'replication_factor':1};"
csql cassandra -u cassandra -p cassandra -e "CREATE TABLE IF NOT EXISTS order_ks.order_table(uuid uuid primary key, customer_id int, source text, quantity int, total float, created_at text);"
