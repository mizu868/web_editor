FROM amazonlinux:2

RUN yum -y update
RUN yum -y upgrade

RUN yum -y install python3-devel
RUN yum -y groupinstall "Development Tools"
RUN pip3 install uwsgi
RUN pip3 install flask
RUN amazon-linux-extras install nginx1

RUN pip3 install timeout-decorator
RUN yum install -y java-1.8.0-openjdk-devel && yum clean all

COPY ./src /opt/src/
COPY ./docker/default.conf /etc/nginx/conf.d/

#起動
RUN chmod 744 /opt/src/server_run.sh
CMD ["/opt/src/server_run.sh"]