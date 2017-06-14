Name     : apache-kafka
Version  : 2.11.0.8.2.2
Release  : 1
URL      : http://mirror.jax.hugeserver.com/apache/kafka/0.8.2.2/kafka_2.11-0.8.2.2.tgz
Source0  : http://mirror.jax.hugeserver.com/apache/kafka/0.8.2.2/kafka_2.11-0.8.2.2.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0

%description
No detailed description available

%prep
%setup -q -n kafka_2.11-0.8.2.2

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/apache-kafka 
cp -r bin  config  libs  LICENSE  NOTICE %{buildroot}/usr/share/apache-kafka

%files
%defattr(-,root,root,-)
/usr/share/apache-kafka/LICENSE
/usr/share/apache-kafka/NOTICE
/usr/share/apache-kafka/bin/kafka-console-consumer.sh
/usr/share/apache-kafka/bin/kafka-console-producer.sh
/usr/share/apache-kafka/bin/kafka-consumer-offset-checker.sh
/usr/share/apache-kafka/bin/kafka-consumer-perf-test.sh
/usr/share/apache-kafka/bin/kafka-mirror-maker.sh
/usr/share/apache-kafka/bin/kafka-preferred-replica-election.sh
/usr/share/apache-kafka/bin/kafka-producer-perf-test.sh
/usr/share/apache-kafka/bin/kafka-reassign-partitions.sh
/usr/share/apache-kafka/bin/kafka-replay-log-producer.sh
/usr/share/apache-kafka/bin/kafka-replica-verification.sh
/usr/share/apache-kafka/bin/kafka-run-class.sh
/usr/share/apache-kafka/bin/kafka-server-start.sh
/usr/share/apache-kafka/bin/kafka-server-stop.sh
/usr/share/apache-kafka/bin/kafka-simple-consumer-shell.sh
/usr/share/apache-kafka/bin/kafka-topics.sh
/usr/share/apache-kafka/bin/windows/kafka-console-consumer.bat
/usr/share/apache-kafka/bin/windows/kafka-console-producer.bat
/usr/share/apache-kafka/bin/windows/kafka-consumer-offset-checker.bat
/usr/share/apache-kafka/bin/windows/kafka-consumer-perf-test.bat
/usr/share/apache-kafka/bin/windows/kafka-mirror-maker.bat
/usr/share/apache-kafka/bin/windows/kafka-preferred-replica-election.bat
/usr/share/apache-kafka/bin/windows/kafka-producer-perf-test.bat
/usr/share/apache-kafka/bin/windows/kafka-reassign-partitions.bat
/usr/share/apache-kafka/bin/windows/kafka-replay-log-producer.bat
/usr/share/apache-kafka/bin/windows/kafka-replica-verification.bat
/usr/share/apache-kafka/bin/windows/kafka-run-class.bat
/usr/share/apache-kafka/bin/windows/kafka-server-start.bat
/usr/share/apache-kafka/bin/windows/kafka-server-stop.bat
/usr/share/apache-kafka/bin/windows/kafka-simple-consumer-shell.bat
/usr/share/apache-kafka/bin/windows/kafka-topics.bat
/usr/share/apache-kafka/bin/windows/zookeeper-server-start.bat
/usr/share/apache-kafka/bin/windows/zookeeper-server-stop.bat
/usr/share/apache-kafka/bin/windows/zookeeper-shell.bat
/usr/share/apache-kafka/bin/zookeeper-server-start.sh
/usr/share/apache-kafka/bin/zookeeper-server-stop.sh
/usr/share/apache-kafka/bin/zookeeper-shell.sh
/usr/share/apache-kafka/config/consumer.properties
/usr/share/apache-kafka/config/log4j.properties
/usr/share/apache-kafka/config/producer.properties
/usr/share/apache-kafka/config/server.properties
/usr/share/apache-kafka/config/test-log4j.properties
/usr/share/apache-kafka/config/tools-log4j.properties
/usr/share/apache-kafka/config/zookeeper.properties
/usr/share/apache-kafka/libs/jopt-simple-3.2.jar
/usr/share/apache-kafka/libs/kafka-clients-0.8.2.2.jar
/usr/share/apache-kafka/libs/kafka_2.11-0.8.2.2-javadoc.jar
/usr/share/apache-kafka/libs/kafka_2.11-0.8.2.2-scaladoc.jar
/usr/share/apache-kafka/libs/kafka_2.11-0.8.2.2-sources.jar
/usr/share/apache-kafka/libs/kafka_2.11-0.8.2.2-test.jar
/usr/share/apache-kafka/libs/kafka_2.11-0.8.2.2.jar
/usr/share/apache-kafka/libs/log4j-1.2.16.jar
/usr/share/apache-kafka/libs/lz4-1.2.0.jar
/usr/share/apache-kafka/libs/metrics-core-2.2.0.jar
/usr/share/apache-kafka/libs/scala-library-2.11.5.jar
/usr/share/apache-kafka/libs/scala-parser-combinators_2.11-1.0.2.jar
/usr/share/apache-kafka/libs/scala-xml_2.11-1.0.2.jar
/usr/share/apache-kafka/libs/slf4j-api-1.7.6.jar
/usr/share/apache-kafka/libs/slf4j-log4j12-1.6.1.jar
/usr/share/apache-kafka/libs/snappy-java-1.1.1.7.jar
/usr/share/apache-kafka/libs/zkclient-0.3.jar
/usr/share/apache-kafka/libs/zookeeper-3.4.6.jar
