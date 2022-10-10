#!/usr/bin/env bash
nginx
cd /opt/src

#CPU / コア数を取得する
CPU=`grep physical.id /proc/cpuinfo | sort -u | wc -l`
CORE=`grep cpu.cores /proc/cpuinfo | sort -u | wc -l`

#uwsgiのプロセス数、スレッド数を設定(要パラメータチューニング)
export UWSGI_THREADS=`expr ${CPU} \* 1`
export UWSGI_PROCESSES=`expr ${CORE} \* 2`
uwsgi --ini app.ini