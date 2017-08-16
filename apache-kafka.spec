Name     : apache-kafka
Version  : 0.10.1.1
Release  : 3
URL      : http://apache.mirrors.lucidnetworks.net/kafka/0.10.1.1/kafka-0.10.1.1-src.tgz
Source0  : http://apache.mirrors.lucidnetworks.net/kafka/0.10.1.1/kafka-0.10.1.1-src.tgz
Source1  : kafka-script
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Patch0   : 0001-Fix-checkstyle-errors.patch
Patch1   : 0002-mavenlocal-repo-config.patch
Patch2   : 0003-Fix-checkstyle-errors-2.patch
Patch3   : 0004-Fix-checkstyle-errors-3.patch
BuildRequires : gradle
BuildRequires : openjdk-dev
BuildRequires : kafka-dep

%description
No detailed description available

%prep
%setup -q -n kafka-0.10.1.1-src
%patch0 -p1
%patch1 -p1 
%patch2 -p1 
%patch3 -p1 

mkdir -p /builddir/.m2
cp -R /usr/share/apache-kafka/.m2/* /builddir/.m2

%build
gradle --offline -PscalaVersion=2.11 releaseTarGz -x signArchives

%check
gradle -PscalaVersion=2.11 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/apache-kafka
tar -xf core/build/distributions/kafka_2.11-0.10.1.1.tgz \
-C %{buildroot}/usr/share/apache-kafka \
--strip 1

# Add helper scripts
mkdir -p %{buildroot}/usr/bin
elements=(kafka-acls.sh kafka-configs.sh kafka-console-consumer.sh \
         kafka-console-producer.sh kafka-consumer-groups.sh \
         kafka-consumer-offset-checker.sh kafka-consumer-perf-test.sh \
         kafka-mirror-maker.sh kafka-preferred-replica-election.sh \
         kafka-producer-perf-test.sh kafka-reassign-partitions.sh \
         kafka-replay-log-producer.sh kafka-replica-verification.sh \
         kafka-run-class.sh kafka-server-start.sh kafka-server-stop.sh \
         kafka-simple-consumer-shell.sh kafka-streams-application-reset.sh \
         kafka-topics.sh kafka-verifiable-consumer.sh \
         kafka-verifiable-producer.sh)
for cmd in "${elements[@]}"
do
    sed s/@@CMD@@/$cmd/ %{SOURCE1} >%{buildroot}/usr/bin/$cmd
    chmod +x %{buildroot}/usr/bin/$cmd
done

%files
%defattr(-,root,root,-)
/usr/bin/kafka-acls.sh
/usr/bin/kafka-configs.sh
/usr/bin/kafka-console-consumer.sh
/usr/bin/kafka-console-producer.sh
/usr/bin/kafka-consumer-groups.sh
/usr/bin/kafka-consumer-offset-checker.sh
/usr/bin/kafka-consumer-perf-test.sh
/usr/bin/kafka-mirror-maker.sh
/usr/bin/kafka-preferred-replica-election.sh
/usr/bin/kafka-producer-perf-test.sh
/usr/bin/kafka-reassign-partitions.sh
/usr/bin/kafka-replay-log-producer.sh
/usr/bin/kafka-replica-verification.sh
/usr/bin/kafka-run-class.sh
/usr/bin/kafka-server-start.sh
/usr/bin/kafka-server-stop.sh
/usr/bin/kafka-simple-consumer-shell.sh
/usr/bin/kafka-streams-application-reset.sh
/usr/bin/kafka-topics.sh
/usr/bin/kafka-verifiable-consumer.sh
/usr/bin/kafka-verifiable-producer.sh
/usr/share/apache-kafka/LICENSE
/usr/share/apache-kafka/NOTICE
/usr/share/apache-kafka/bin/connect-distributed.sh
/usr/share/apache-kafka/bin/connect-standalone.sh
/usr/share/apache-kafka/bin/kafka-acls.sh
/usr/share/apache-kafka/bin/kafka-configs.sh
/usr/share/apache-kafka/bin/kafka-console-consumer.sh
/usr/share/apache-kafka/bin/kafka-console-producer.sh
/usr/share/apache-kafka/bin/kafka-consumer-groups.sh
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
/usr/share/apache-kafka/bin/kafka-streams-application-reset.sh
/usr/share/apache-kafka/bin/kafka-topics.sh
/usr/share/apache-kafka/bin/kafka-verifiable-consumer.sh
/usr/share/apache-kafka/bin/kafka-verifiable-producer.sh
/usr/share/apache-kafka/bin/windows/kafka-acls.bat
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
/usr/share/apache-kafka/bin/zookeeper-security-migration.sh
/usr/share/apache-kafka/bin/zookeeper-server-start.sh
/usr/share/apache-kafka/bin/zookeeper-server-stop.sh
/usr/share/apache-kafka/bin/zookeeper-shell.sh
/usr/share/apache-kafka/config/connect-console-sink.properties
/usr/share/apache-kafka/config/connect-console-source.properties
/usr/share/apache-kafka/config/connect-distributed.properties
/usr/share/apache-kafka/config/connect-file-sink.properties
/usr/share/apache-kafka/config/connect-file-source.properties
/usr/share/apache-kafka/config/connect-log4j.properties
/usr/share/apache-kafka/config/connect-standalone.properties
/usr/share/apache-kafka/config/consumer.properties
/usr/share/apache-kafka/config/log4j.properties
/usr/share/apache-kafka/config/producer.properties
/usr/share/apache-kafka/config/server.properties
/usr/share/apache-kafka/config/tools-log4j.properties
/usr/share/apache-kafka/config/zookeeper.properties
/usr/share/apache-kafka/libs/aopalliance-repackaged-2.4.0-b34.jar
/usr/share/apache-kafka/libs/argparse4j-0.5.0.jar
/usr/share/apache-kafka/libs/connect-api-0.10.1.1.jar
/usr/share/apache-kafka/libs/connect-file-0.10.1.1.jar
/usr/share/apache-kafka/libs/connect-json-0.10.1.1.jar
/usr/share/apache-kafka/libs/connect-runtime-0.10.1.1.jar
/usr/share/apache-kafka/libs/guava-18.0.jar
/usr/share/apache-kafka/libs/hk2-api-2.4.0-b34.jar
/usr/share/apache-kafka/libs/hk2-locator-2.4.0-b34.jar
/usr/share/apache-kafka/libs/hk2-utils-2.4.0-b34.jar
/usr/share/apache-kafka/libs/jackson-annotations-2.6.0.jar
/usr/share/apache-kafka/libs/jackson-core-2.6.3.jar
/usr/share/apache-kafka/libs/jackson-databind-2.6.3.jar
/usr/share/apache-kafka/libs/jackson-jaxrs-base-2.6.3.jar
/usr/share/apache-kafka/libs/jackson-jaxrs-json-provider-2.6.3.jar
/usr/share/apache-kafka/libs/jackson-module-jaxb-annotations-2.6.3.jar
/usr/share/apache-kafka/libs/javassist-3.18.2-GA.jar
/usr/share/apache-kafka/libs/javax.annotation-api-1.2.jar
/usr/share/apache-kafka/libs/javax.inject-1.jar
/usr/share/apache-kafka/libs/javax.inject-2.4.0-b34.jar
/usr/share/apache-kafka/libs/javax.servlet-api-3.1.0.jar
/usr/share/apache-kafka/libs/javax.ws.rs-api-2.0.1.jar
/usr/share/apache-kafka/libs/jersey-client-2.22.2.jar
/usr/share/apache-kafka/libs/jersey-common-2.22.2.jar
/usr/share/apache-kafka/libs/jersey-container-servlet-2.22.2.jar
/usr/share/apache-kafka/libs/jersey-container-servlet-core-2.22.2.jar
/usr/share/apache-kafka/libs/jersey-guava-2.22.2.jar
/usr/share/apache-kafka/libs/jersey-media-jaxb-2.22.2.jar
/usr/share/apache-kafka/libs/jersey-server-2.22.2.jar
/usr/share/apache-kafka/libs/jetty-continuation-9.2.15.v20160210.jar
/usr/share/apache-kafka/libs/jetty-http-9.2.15.v20160210.jar
/usr/share/apache-kafka/libs/jetty-io-9.2.15.v20160210.jar
/usr/share/apache-kafka/libs/jetty-security-9.2.15.v20160210.jar
/usr/share/apache-kafka/libs/jetty-server-9.2.15.v20160210.jar
/usr/share/apache-kafka/libs/jetty-servlet-9.2.15.v20160210.jar
/usr/share/apache-kafka/libs/jetty-servlets-9.2.15.v20160210.jar
/usr/share/apache-kafka/libs/jetty-util-9.2.15.v20160210.jar
/usr/share/apache-kafka/libs/jopt-simple-4.9.jar
/usr/share/apache-kafka/libs/kafka-clients-0.10.1.1.jar
/usr/share/apache-kafka/libs/kafka-log4j-appender-0.10.1.1.jar
/usr/share/apache-kafka/libs/kafka-streams-0.10.1.1.jar
/usr/share/apache-kafka/libs/kafka-streams-examples-0.10.1.1.jar
/usr/share/apache-kafka/libs/kafka-tools-0.10.1.1.jar
/usr/share/apache-kafka/libs/kafka_2.11-0.10.1.1-javadoc.jar
/usr/share/apache-kafka/libs/kafka_2.11-0.10.1.1-scaladoc.jar
/usr/share/apache-kafka/libs/kafka_2.11-0.10.1.1-sources.jar
/usr/share/apache-kafka/libs/kafka_2.11-0.10.1.1-test-sources.jar
/usr/share/apache-kafka/libs/kafka_2.11-0.10.1.1-test.jar
/usr/share/apache-kafka/libs/kafka_2.11-0.10.1.1.jar
/usr/share/apache-kafka/libs/log4j-1.2.17.jar
/usr/share/apache-kafka/libs/lz4-1.3.0.jar
/usr/share/apache-kafka/libs/metrics-core-2.2.0.jar
/usr/share/apache-kafka/libs/osgi-resource-locator-1.0.1.jar
/usr/share/apache-kafka/libs/reflections-0.9.10.jar
/usr/share/apache-kafka/libs/rocksdbjni-4.9.0.jar
/usr/share/apache-kafka/libs/scala-library-2.11.8.jar
/usr/share/apache-kafka/libs/scala-parser-combinators_2.11-1.0.4.jar
/usr/share/apache-kafka/libs/slf4j-api-1.7.21.jar
/usr/share/apache-kafka/libs/slf4j-log4j12-1.7.21.jar
/usr/share/apache-kafka/libs/snappy-java-1.1.2.6.jar
/usr/share/apache-kafka/libs/validation-api-1.1.0.Final.jar
/usr/share/apache-kafka/libs/zkclient-0.9.jar
/usr/share/apache-kafka/libs/zookeeper-3.4.8.jar
/usr/share/apache-kafka/site-docs/kafka_2.11-0.10.1.1-site-docs.tgz
