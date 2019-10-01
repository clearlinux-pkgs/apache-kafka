#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : apache-kafka
Version  : 2.3.0
Release  : 12
URL      : https://github.com/apache/kafka/archive/2.3.0.tar.gz
Source0  : https://github.com/apache/kafka/archive/2.3.0.tar.gz
Source1  : apache-kafka.service
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause CDDL-1.1
Requires: apache-kafka-bin = %{version}-%{release}
Requires: apache-kafka-data = %{version}-%{release}
Requires: apache-kafka-license = %{version}-%{release}
Requires: apache-kafka-services = %{version}-%{release}
Requires: requests
BuildRequires : apache-maven
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-mvn
BuildRequires : gradle
BuildRequires : mvn(cglib:cglib-nodep:jar) = 3.2.9
BuildRequires : mvn(com.101tec:zkclient:jar) = 0.11
BuildRequires : mvn(com.diffplug.durian:durian-collect:jar) = 1.2.0
BuildRequires : mvn(com.diffplug.durian:durian-core:jar) = 1.2.0
BuildRequires : mvn(com.diffplug.durian:durian-io:jar) = 1.2.0
BuildRequires : mvn(com.diffplug.spotless:spotless-plugin-gradle:jar) = 3.23.0
BuildRequires : mvn(com.esotericsoftware:minlog:jar) = 1.3
BuildRequires : mvn(com.fasterxml.jackson.core:jackson-annotations:jar) = 2.9.0
BuildRequires : mvn(com.fasterxml.jackson.core:jackson-annotations:jar) = 2.9.9
BuildRequires : mvn(com.fasterxml.jackson.core:jackson-core:jar) = 2.9.9
BuildRequires : mvn(com.fasterxml.jackson.core:jackson-databind:jar) = 2.9.9
BuildRequires : mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-csv:jar) = 2.9.9
BuildRequires : mvn(com.fasterxml.jackson.datatype:jackson-datatype-jdk8:jar) = 2.9.9
BuildRequires : mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-json-provider:jar) = 2.9.9
BuildRequires : mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-providers:pom) = 2.9.9
BuildRequires : mvn(com.fasterxml.jackson.module:jackson-module-jaxb-annotations:jar) = 2.9.9
BuildRequires : mvn(com.fasterxml.jackson.module:jackson-module-paranamer:jar) = 2.9.9
BuildRequires : mvn(com.fasterxml.jackson.module:jackson-module-scala_2.12:jar) = 2.9.9
BuildRequires : mvn(com.fasterxml.jackson.module:jackson-modules-base:pom) = 2.9.9
BuildRequires : mvn(com.fasterxml.jackson.module:jackson-modules-java8:pom) = 2.9.9
BuildRequires : mvn(com.fasterxml.jackson:jackson-base:pom) = 2.9.9
BuildRequires : mvn(com.fasterxml.jackson:jackson-bom:pom) = 2.9.9
BuildRequires : mvn(com.fasterxml.jackson:jackson-parent:pom) = 2.9.1.2
BuildRequires : mvn(com.github.luben:zstd-jni:jar) = 1.4.0.1
BuildRequires : mvn(com.github.spullara.mustache.java:compiler:jar) = 0.8.17
BuildRequires : mvn(com.google.guava:guava:jar) = 27.0.1.jre
BuildRequires : mvn(com.googlecode.concurrent-trees:concurrent-trees:jar) = 2.6.1
BuildRequires : mvn(com.googlecode.javaewah:JavaEWAH:jar) = 1.1.6
BuildRequires : mvn(com.h2database:h2:jar) = 1.4.196
BuildRequires : mvn(com.h3xstream.retirejs:retirejs-core:jar) = 3.0.1
BuildRequires : mvn(com.h3xstream.retirejs:retirejs-root-pom:pom) = 3.0.1
BuildRequires : mvn(com.jcraft:jzlib:jar) = 1.1.1
BuildRequires : mvn(com.sun.mail:all:pom) = 1.6.3
BuildRequires : mvn(com.sun.mail:mailapi:jar) = 1.6.3
BuildRequires : mvn(com.thoughtworks.paranamer:paranamer:jar) = 2.8
BuildRequires : mvn(com.typesafe.sbt:compiler-interface:pom) = 0.13.15
BuildRequires : mvn(com.typesafe.sbt:incremental-compiler:jar) = 0.13.15
BuildRequires : mvn(com.typesafe.sbt:sbt-interface:jar) = 0.13.15
BuildRequires : mvn(com.typesafe.scala-logging:scala-logging_2.12:jar) = 3.9.0
BuildRequires : mvn(com.typesafe.zinc:zinc:jar) = 0.3.15
BuildRequires : mvn(com.vdurmont:semver4j:jar) = 2.2.0
BuildRequires : mvn(com.yammer.metrics:metrics-core:jar) = 2.2.0
BuildRequires : mvn(commons-codec:commons-codec:jar) = 1.11
BuildRequires : mvn(commons-logging:commons-logging:jar) = 1.2
BuildRequires : mvn(commons-pool:commons-pool:jar) = 1.6
BuildRequires : mvn(gradle.plugin.com.github.spotbugs:spotbugs-gradle-plugin:jar) = 1.6.9
BuildRequires : mvn(jakarta.annotation:jakarta.annotation-api:jar) = 1.3.4
BuildRequires : mvn(jakarta.ws.rs:jakarta.ws.rs-api:jar) = 2.1.5
BuildRequires : mvn(javax.activation:activation:jar) = 1.1.1
BuildRequires : mvn(javax.servlet:javax.servlet-api:jar) = 3.1.0
BuildRequires : mvn(javax.validation:validation-api:jar) = 2.0.1.Final
BuildRequires : mvn(javax.ws.rs:javax.ws.rs-api:jar) = 2.1.1
BuildRequires : mvn(javax.xml.bind:jaxb-api-parent:pom) = 2.3.0
BuildRequires : mvn(javax.xml.bind:jaxb-api:jar) = 2.3.0
BuildRequires : mvn(jfree:jfreechart:jar) = 1.0.0
BuildRequires : mvn(jfreechart:jfreechart:jar) = 1.0.0
BuildRequires : mvn(joda-time:joda-time:jar) = 1.6
BuildRequires : mvn(junit:junit:jar) = 4.13.beta.2
BuildRequires : mvn(log4j:log4j:jar) = 1.2.17
BuildRequires : mvn(net.bytebuddy:byte-buddy-agent:jar) = 1.9.10
BuildRequires : mvn(net.bytebuddy:byte-buddy-agent:jar) = 1.9.3
BuildRequires : mvn(net.bytebuddy:byte-buddy-parent:pom) = 1.9.10
BuildRequires : mvn(net.bytebuddy:byte-buddy:jar) = 1.9.10
BuildRequires : mvn(net.bytebuddy:byte-buddy:jar) = 1.9.3
BuildRequires : mvn(net.sf.ehcache:ehcache-parent:pom) = 2.18
BuildRequires : mvn(net.sf.ehcache:ehcache-root:pom) = 2.10.4
BuildRequires : mvn(net.sf.ehcache:ehcache:jar) = 2.10.4
BuildRequires : mvn(net.sf.jopt-simple:jopt-simple:jar) = 5.0.4
BuildRequires : mvn(net.sourceforge.argparse4j:argparse4j:jar) = 0.7.0
BuildRequires : mvn(org.ajoberstar.grgit:grgit-core:jar) = 3.1.1
BuildRequires : mvn(org.apache.commons:commons-parent:pom) = 45
BuildRequires : mvn(org.apache.commons:commons-text:jar) = 1.3
BuildRequires : mvn(org.apache.directory.api:api-all:jar) = 1.0.2
BuildRequires : mvn(org.apache.directory.api:api-asn1-api:jar) = 1.0.0
BuildRequires : mvn(org.apache.directory.api:api-asn1-ber:jar) = 1.0.0
BuildRequires : mvn(org.apache.directory.api:api-i18n:jar) = 1.0.0
BuildRequires : mvn(org.apache.directory.api:api-ldap-client-api:jar) = 1.0.0
BuildRequires : mvn(org.apache.directory.api:api-ldap-client-parent:pom) = 1.0.0
BuildRequires : mvn(org.apache.directory.api:api-ldap-codec-core:jar) = 1.0.0
BuildRequires : mvn(org.apache.directory.api:api-ldap-codec-parent:pom) = 1.0.0
BuildRequires : mvn(org.apache.directory.api:api-ldap-extras-aci:jar) = 1.0.0
BuildRequires : mvn(org.apache.directory.api:api-ldap-extras-codec-api:jar) = 1.0.0
BuildRequires : mvn(org.apache.directory.api:api-ldap-extras-codec:jar) = 1.0.0
BuildRequires : mvn(org.apache.directory.api:api-ldap-extras-parent:pom) = 1.0.0
BuildRequires : mvn(org.apache.directory.api:api-ldap-extras-sp:jar) = 1.0.0
BuildRequires : mvn(org.apache.directory.api:api-ldap-extras-trigger:jar) = 1.0.0
BuildRequires : mvn(org.apache.directory.api:api-ldap-extras-util:jar) = 1.0.0
BuildRequires : mvn(org.apache.directory.api:api-ldap-model:jar) = 1.0.0
BuildRequires : mvn(org.apache.directory.api:api-ldap-parent:pom) = 1.0.0
BuildRequires : mvn(org.apache.directory.api:api-parent:pom) = 1.0.2
BuildRequires : mvn(org.apache.directory.api:api-util:jar) = 1.0.0
BuildRequires : mvn(org.apache.directory.jdbm:apacheds-jdbm1:jar) = 2.0.0.M3
BuildRequires : mvn(org.apache.directory.mavibot:mavibot:jar) = 1.0.0.M8
BuildRequires : mvn(org.apache.directory.project:project:pom) = 40
BuildRequires : mvn(org.apache.directory.project:project:pom) = 41
BuildRequires : mvn(org.apache.directory.server:apacheds-core-api:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-core-avl:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-core-constants:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-core-shared:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-interceptor-kerberos:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-interceptors-admin:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-interceptors-authn:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-interceptors-authz:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-interceptors-changelog:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-interceptors-collective:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-interceptors-event:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-interceptors-exception:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-interceptors-journal:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-interceptors-normalization:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-interceptors-number:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-interceptors-operational:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-interceptors-referral:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-interceptors-schema:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-interceptors-subtree:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-interceptors-trigger:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-jdbm-partition:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-kerberos-codec:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-ldif-partition:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-mavibot-partition:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-parent:pom) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-protocol-kerberos:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-protocol-ldap:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-protocol-shared:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.directory.server:apacheds-xdbm-partition:jar) = 2.0.0.M24
BuildRequires : mvn(org.apache.httpcomponents:httpclient:jar) = 4.5.8
BuildRequires : mvn(org.apache.httpcomponents:httpcomponents-client:pom) = 4.5.8
BuildRequires : mvn(org.apache.httpcomponents:httpcomponents-parent:pom) = 11
BuildRequires : mvn(org.apache.httpcomponents:httpcore:jar) = 4.4.11
BuildRequires : mvn(org.apache.lucene:lucene-analyzers-common:jar) = 7.6.0
BuildRequires : mvn(org.apache.lucene:lucene-core:jar) = 7.6.0
BuildRequires : mvn(org.apache.lucene:lucene-parent:pom) = 7.6.0
BuildRequires : mvn(org.apache.lucene:lucene-queries:jar) = 7.6.0
BuildRequires : mvn(org.apache.lucene:lucene-queryparser:jar) = 7.6.0
BuildRequires : mvn(org.apache.lucene:lucene-sandbox:jar) = 7.6.0
BuildRequires : mvn(org.apache.lucene:lucene-solr-grandparent:pom) = 7.6.0
BuildRequires : mvn(org.apache.maven:maven-artifact:jar) = 3.6.1
BuildRequires : mvn(org.apache.maven:maven-parent:pom) = 33
BuildRequires : mvn(org.apache.maven:maven:pom) = 3.6.1
BuildRequires : mvn(org.apache.mina:mina-core:jar) = 2.0.16
BuildRequires : mvn(org.apache.servicemix.bundles:bundles-pom:pom) = 11
BuildRequires : mvn(org.apache.servicemix.bundles:org.apache.servicemix.bundles.antlr:jar) = 2.7.7_5
BuildRequires : mvn(org.apache.servicemix.bundles:org.apache.servicemix.bundles.dom4j:jar) = 1.6.1_5
BuildRequires : mvn(org.apache.servicemix.bundles:org.apache.servicemix.bundles.xpp3:jar) = 1.1.4c_7
BuildRequires : mvn(org.apache.servicemix:servicemix-pom:pom) = 5
BuildRequires : mvn(org.apache.yetus:audience-annotations:jar) = 0.5.0
BuildRequires : mvn(org.apache.zookeeper:zookeeper:jar) = 3.4.14
BuildRequires : mvn(org.bouncycastle:bcpg-jdk15on:jar) = 1.60
BuildRequires : mvn(org.bouncycastle:bcpkix-jdk15on:jar) = 1.60
BuildRequires : mvn(org.bouncycastle:bcpkix-jdk15on:jar) = 1.61
BuildRequires : mvn(org.bouncycastle:bcprov-jdk15on:jar) = 1.60
BuildRequires : mvn(org.checkerframework:checker-qual:jar) = 2.5.2
BuildRequires : mvn(org.codehaus.groovy:groovy-backports-compat23:jar) = 2.4.15
BuildRequires : mvn(org.codehaus.mojo:animal-sniffer-annotations:jar) = 1.17
BuildRequires : mvn(org.codehaus.mojo:animal-sniffer-parent:pom) = 1.17
BuildRequires : mvn(org.codehaus.mojo:mojo-parent:pom) = 40
BuildRequires : mvn(org.codehaus.plexus:plexus-utils:jar) = 3.2.0
BuildRequires : mvn(org.codehaus.plexus:plexus:pom) = 5.1
BuildRequires : mvn(org.easymock:easymock:jar) = 4.0.2
BuildRequires : mvn(org.eclipse.ee4j:project:pom) = 1.0.4
BuildRequires : mvn(org.eclipse.ee4j:project:pom) = 1.0.5
BuildRequires : mvn(org.eclipse.jetty:jetty-client:jar) = 9.4.18.v20190429
BuildRequires : mvn(org.eclipse.jetty:jetty-continuation:jar) = 9.4.18.v20190429
BuildRequires : mvn(org.eclipse.jetty:jetty-http:jar) = 9.4.18.v20190429
BuildRequires : mvn(org.eclipse.jetty:jetty-io:jar) = 9.4.18.v20190429
BuildRequires : mvn(org.eclipse.jetty:jetty-project:pom) = 9.4.18.v20190429
BuildRequires : mvn(org.eclipse.jetty:jetty-security:jar) = 9.4.18.v20190429
BuildRequires : mvn(org.eclipse.jetty:jetty-server:jar) = 9.4.18.v20190429
BuildRequires : mvn(org.eclipse.jetty:jetty-servlet:jar) = 9.4.18.v20190429
BuildRequires : mvn(org.eclipse.jetty:jetty-servlets:jar) = 9.4.18.v20190429
BuildRequires : mvn(org.eclipse.jetty:jetty-util:jar) = 9.4.18.v20190429
BuildRequires : mvn(org.glassfish.hk2.external:aopalliance-repackaged:jar) = 2.5.0
BuildRequires : mvn(org.glassfish.hk2.external:jakarta.inject:jar) = 2.5.0
BuildRequires : mvn(org.glassfish.hk2:external:pom) = 2.5.0
BuildRequires : mvn(org.glassfish.hk2:hk2-api:jar) = 2.5.0
BuildRequires : mvn(org.glassfish.hk2:hk2-bom:pom) = 2.5.0
BuildRequires : mvn(org.glassfish.hk2:hk2-locator:jar) = 2.5.0
BuildRequires : mvn(org.glassfish.hk2:hk2-parent:pom) = 2.5.0
BuildRequires : mvn(org.glassfish.hk2:hk2-utils:jar) = 2.5.0
BuildRequires : mvn(org.glassfish.hk2:osgi-resource-locator:jar) = 1.0.1
BuildRequires : mvn(org.glassfish.jersey.containers:jersey-container-servlet-core:jar) = 2.28
BuildRequires : mvn(org.glassfish.jersey.containers:jersey-container-servlet:jar) = 2.28
BuildRequires : mvn(org.glassfish.jersey.containers:project:pom) = 2.28
BuildRequires : mvn(org.glassfish.jersey.core:jersey-client:jar) = 2.28
BuildRequires : mvn(org.glassfish.jersey.core:jersey-common:jar) = 2.28
BuildRequires : mvn(org.glassfish.jersey.core:jersey-server:jar) = 2.28
BuildRequires : mvn(org.glassfish.jersey.inject:jersey-hk2:jar) = 2.28
BuildRequires : mvn(org.glassfish.jersey.inject:project:pom) = 2.28
BuildRequires : mvn(org.glassfish.jersey.media:jersey-media-jaxb:jar) = 2.28
BuildRequires : mvn(org.glassfish.jersey.media:project:pom) = 2.28
BuildRequires : mvn(org.glassfish.jersey:project:pom) = 2.28
BuildRequires : mvn(org.glassfish:javax.json:jar) = 1.0.4
BuildRequires : mvn(org.hamcrest:hamcrest-core:jar) = 1.3
BuildRequires : mvn(org.hamcrest:hamcrest:jar) = 2.1
BuildRequires : mvn(org.javassist:javassist:jar) = 3.22.0.CR2
BuildRequires : mvn(org.javassist:javassist:jar) = 3.24.0.GA
BuildRequires : mvn(org.json:json:jar) = 20140107
BuildRequires : mvn(org.jsoup:jsoup:jar) = 1.11.3
BuildRequires : mvn(org.lz4:lz4-java:jar) = 1.6.0
BuildRequires : mvn(org.mockito:mockito-core:jar) = 2.27.0
BuildRequires : mvn(org.objenesis:objenesis:jar) = 2.6
BuildRequires : mvn(org.objenesis:objenesis:jar) = 3.0.1
BuildRequires : mvn(org.owasp:dependency-check-core:jar) = 4.0.2
BuildRequires : mvn(org.owasp:dependency-check-utils:jar) = 4.0.2
BuildRequires : mvn(org.powermock:powermock-api-easymock:jar) = 2.0.2
BuildRequires : mvn(org.powermock:powermock-api-support:jar) = 2.0.2
BuildRequires : mvn(org.powermock:powermock-core:jar) = 2.0.2
BuildRequires : mvn(org.powermock:powermock-module-junit4-common:jar) = 2.0.2
BuildRequires : mvn(org.powermock:powermock-module-junit4:jar) = 2.0.2
BuildRequires : mvn(org.powermock:powermock-reflect:jar) = 2.0.2
BuildRequires : mvn(org.reflections:reflections:jar) = 0.9.11
BuildRequires : mvn(org.rocksdb:rocksdbjni:jar) = 5.18.3
BuildRequires : mvn(org.scala-lang.modules:scala-xml_2.12:jar) = 1.0.5
BuildRequires : mvn(org.scala-lang.modules:scala-xml_2.12:jar) = 1.1.0
BuildRequires : mvn(org.scala-lang:scala-compiler:jar) = 2.12.8
BuildRequires : mvn(org.scala-lang:scala-library:jar) = 2.12.3
BuildRequires : mvn(org.scala-lang:scala-library:jar) = 2.12.8
BuildRequires : mvn(org.scala-lang:scala-reflect:jar) = 2.12.8
BuildRequires : mvn(org.scalactic:scalactic_2.12:jar) = 3.0.7
BuildRequires : mvn(org.scalatest:scalatest_2.12:jar) = 3.0.7
BuildRequires : mvn(org.scoverage:scalac-scoverage-plugin_2.12:jar) = 1.3.1
BuildRequires : mvn(org.scoverage:scalac-scoverage-runtime_2.12:jar) = 1.3.1
BuildRequires : mvn(org.slf4j:slf4j-log4j12:jar) = 1.7.26
BuildRequires : mvn(org.xerial.snappy:snappy-java:jar) = 1.1.7.3
BuildRequires : mvn-JavaEWAH
BuildRequires : mvn-apache
BuildRequires : mvn-commons-collections
BuildRequires : mvn-commons-compress
BuildRequires : mvn-commons-io
BuildRequires : mvn-commons-lang
BuildRequires : mvn-commons-lang3
BuildRequires : mvn-commons-parent
BuildRequires : mvn-commons-text
BuildRequires : mvn-dependency-check-gradle
BuildRequires : mvn-gradle-scoverage
BuildRequires : mvn-gradle-versions-plugin
BuildRequires : mvn-gson
BuildRequires : mvn-guava
BuildRequires : mvn-jgit
BuildRequires : mvn-joda-time
BuildRequires : mvn-jsch
BuildRequires : mvn-jsoup
BuildRequires : mvn-oss-parents
BuildRequires : mvn-shadow
BuildRequires : mvn-spotbugs
BuildRequires : mvn-velocity
BuildRequires : mvn-xmlpull
BuildRequires : mvn-xpp3_min
BuildRequires : mvn-xstream
BuildRequires : requests
Patch1: Stateless.patch
Patch2: kafka-script.patch

%description
This directory contains examples of client code that uses kafka.
To run the demo:

%package bin
Summary: bin components for the apache-kafka package.
Group: Binaries
Requires: apache-kafka-data = %{version}-%{release}
Requires: apache-kafka-license = %{version}-%{release}
Requires: apache-kafka-services = %{version}-%{release}

%description bin
bin components for the apache-kafka package.


%package data
Summary: data components for the apache-kafka package.
Group: Data

%description data
data components for the apache-kafka package.


%package license
Summary: license components for the apache-kafka package.
Group: Default

%description license
license components for the apache-kafka package.


%package services
Summary: services components for the apache-kafka package.
Group: Systemd services

%description services
services components for the apache-kafka package.


%prep
%setup -q -n kafka-2.3.0
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
mkdir -p %{buildroot}
mkdir -p ~/.m2
cp -r /usr/share/java/.m2/* ~/.m2/ || :
find . -type f '(' -name '*.gradle' -o -name '*.gradle.kts' ')' -exec sed -i 's|\(repositories\s*{\)|\1\n    mavenLocal()|' {} +
gradle --offline dependencies || :
gradle --offline -PscalaVersion=2.12 releaseTarGz -x signArchives

%install

mkdir -p %{buildroot}/usr/share/package-licenses/apache-kafka
cp LICENSE %{buildroot}/usr/share/package-licenses/apache-kafka/LICENSE
cp NOTICE %{buildroot}/usr/share/package-licenses/apache-kafka/NOTICE
gradle --offline
if [[ -d build/install ]]; then
pushd build/install
shopt -s nullglob
for lib_dir in */lib; do
pushd ${lib_dir}
for jarfile in *.jar; do
JARNAME=$(basename ${jarfile})
REALJAR=$(find /usr/share/java/.m2/repository -type f -name "${JARNAME}")
if ! [[ -z ${REALJAR} ]]; then
ln -sf ${REALJAR/#\/usr\/share\/java/..\/..}
fi
done
popd
done
find . -type f -name '*.bat' -exec rm -f {} +
mkdir -p %{buildroot}/usr/share/java/apache-kafka
cp -r * %{buildroot}/usr/share/java/apache-kafka
popd
fi
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/apache-kafka.service
## install_append content
mkdir -p %{buildroot}/usr/share/apache-kafka
tar -xf core/build/distributions/kafka_2.12-2.3.0.tgz \
-C %{buildroot}/usr/share/apache-kafka \
--strip 1
mkdir -p %{buildroot}/usr/share/defaults/kafka
mv %{buildroot}/usr/share/apache-kafka/config/* %{buildroot}/usr/share/defaults/kafka
rm -rf %{buildroot}/usr/share/apache-kafka/bin/windows
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
sed s/@@CMD@@/$cmd/ kafka-script >%{buildroot}/usr/bin/$cmd
chmod +x %{buildroot}/usr/bin/$cmd
done
## install_append end

%files
%defattr(-,root,root,-)

%files bin
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

%files data
%defattr(-,root,root,-)
/usr/share/apache-kafka/LICENSE
/usr/share/apache-kafka/NOTICE
/usr/share/apache-kafka/bin/connect-distributed.sh
/usr/share/apache-kafka/bin/connect-standalone.sh
/usr/share/apache-kafka/bin/kafka-acls.sh
/usr/share/apache-kafka/bin/kafka-broker-api-versions.sh
/usr/share/apache-kafka/bin/kafka-configs.sh
/usr/share/apache-kafka/bin/kafka-console-consumer.sh
/usr/share/apache-kafka/bin/kafka-console-producer.sh
/usr/share/apache-kafka/bin/kafka-consumer-groups.sh
/usr/share/apache-kafka/bin/kafka-consumer-perf-test.sh
/usr/share/apache-kafka/bin/kafka-delegation-tokens.sh
/usr/share/apache-kafka/bin/kafka-delete-records.sh
/usr/share/apache-kafka/bin/kafka-dump-log.sh
/usr/share/apache-kafka/bin/kafka-log-dirs.sh
/usr/share/apache-kafka/bin/kafka-mirror-maker.sh
/usr/share/apache-kafka/bin/kafka-preferred-replica-election.sh
/usr/share/apache-kafka/bin/kafka-producer-perf-test.sh
/usr/share/apache-kafka/bin/kafka-reassign-partitions.sh
/usr/share/apache-kafka/bin/kafka-replica-verification.sh
/usr/share/apache-kafka/bin/kafka-run-class.sh
/usr/share/apache-kafka/bin/kafka-server-start.sh
/usr/share/apache-kafka/bin/kafka-server-stop.sh
/usr/share/apache-kafka/bin/kafka-streams-application-reset.sh
/usr/share/apache-kafka/bin/kafka-topics.sh
/usr/share/apache-kafka/bin/kafka-verifiable-consumer.sh
/usr/share/apache-kafka/bin/kafka-verifiable-producer.sh
/usr/share/apache-kafka/bin/trogdor.sh
/usr/share/apache-kafka/bin/zookeeper-security-migration.sh
/usr/share/apache-kafka/bin/zookeeper-server-start.sh
/usr/share/apache-kafka/bin/zookeeper-server-stop.sh
/usr/share/apache-kafka/bin/zookeeper-shell.sh
/usr/share/apache-kafka/libs/activation-1.1.1.jar
/usr/share/apache-kafka/libs/aopalliance-repackaged-2.5.0.jar
/usr/share/apache-kafka/libs/argparse4j-0.7.0.jar
/usr/share/apache-kafka/libs/audience-annotations-0.5.0.jar
/usr/share/apache-kafka/libs/commons-lang3-3.8.1.jar
/usr/share/apache-kafka/libs/connect-api-2.3.0.jar
/usr/share/apache-kafka/libs/connect-basic-auth-extension-2.3.0.jar
/usr/share/apache-kafka/libs/connect-file-2.3.0.jar
/usr/share/apache-kafka/libs/connect-json-2.3.0.jar
/usr/share/apache-kafka/libs/connect-runtime-2.3.0.jar
/usr/share/apache-kafka/libs/connect-transforms-2.3.0.jar
/usr/share/apache-kafka/libs/guava-20.0.jar
/usr/share/apache-kafka/libs/hk2-api-2.5.0.jar
/usr/share/apache-kafka/libs/hk2-locator-2.5.0.jar
/usr/share/apache-kafka/libs/hk2-utils-2.5.0.jar
/usr/share/apache-kafka/libs/jackson-annotations-2.9.9.jar
/usr/share/apache-kafka/libs/jackson-core-2.9.9.jar
/usr/share/apache-kafka/libs/jackson-databind-2.9.9.jar
/usr/share/apache-kafka/libs/jackson-dataformat-csv-2.9.9.jar
/usr/share/apache-kafka/libs/jackson-datatype-jdk8-2.9.9.jar
/usr/share/apache-kafka/libs/jackson-jaxrs-base-2.9.9.jar
/usr/share/apache-kafka/libs/jackson-jaxrs-json-provider-2.9.9.jar
/usr/share/apache-kafka/libs/jackson-module-jaxb-annotations-2.9.9.jar
/usr/share/apache-kafka/libs/jackson-module-paranamer-2.9.9.jar
/usr/share/apache-kafka/libs/jackson-module-scala_2.12-2.9.9.jar
/usr/share/apache-kafka/libs/jakarta.annotation-api-1.3.4.jar
/usr/share/apache-kafka/libs/jakarta.inject-2.5.0.jar
/usr/share/apache-kafka/libs/jakarta.ws.rs-api-2.1.5.jar
/usr/share/apache-kafka/libs/javassist-3.22.0-CR2.jar
/usr/share/apache-kafka/libs/javax.servlet-api-3.1.0.jar
/usr/share/apache-kafka/libs/javax.ws.rs-api-2.1.1.jar
/usr/share/apache-kafka/libs/jaxb-api-2.3.0.jar
/usr/share/apache-kafka/libs/jersey-client-2.28.jar
/usr/share/apache-kafka/libs/jersey-common-2.28.jar
/usr/share/apache-kafka/libs/jersey-container-servlet-2.28.jar
/usr/share/apache-kafka/libs/jersey-container-servlet-core-2.28.jar
/usr/share/apache-kafka/libs/jersey-hk2-2.28.jar
/usr/share/apache-kafka/libs/jersey-media-jaxb-2.28.jar
/usr/share/apache-kafka/libs/jersey-server-2.28.jar
/usr/share/apache-kafka/libs/jetty-client-9.4.18.v20190429.jar
/usr/share/apache-kafka/libs/jetty-continuation-9.4.18.v20190429.jar
/usr/share/apache-kafka/libs/jetty-http-9.4.18.v20190429.jar
/usr/share/apache-kafka/libs/jetty-io-9.4.18.v20190429.jar
/usr/share/apache-kafka/libs/jetty-security-9.4.18.v20190429.jar
/usr/share/apache-kafka/libs/jetty-server-9.4.18.v20190429.jar
/usr/share/apache-kafka/libs/jetty-servlet-9.4.18.v20190429.jar
/usr/share/apache-kafka/libs/jetty-servlets-9.4.18.v20190429.jar
/usr/share/apache-kafka/libs/jetty-util-9.4.18.v20190429.jar
/usr/share/apache-kafka/libs/jopt-simple-5.0.4.jar
/usr/share/apache-kafka/libs/jsr305-3.0.2.jar
/usr/share/apache-kafka/libs/kafka-clients-2.3.0.jar
/usr/share/apache-kafka/libs/kafka-log4j-appender-2.3.0.jar
/usr/share/apache-kafka/libs/kafka-streams-2.3.0.jar
/usr/share/apache-kafka/libs/kafka-streams-examples-2.3.0.jar
/usr/share/apache-kafka/libs/kafka-streams-scala_2.12-2.3.0.jar
/usr/share/apache-kafka/libs/kafka-streams-test-utils-2.3.0.jar
/usr/share/apache-kafka/libs/kafka-tools-2.3.0.jar
/usr/share/apache-kafka/libs/kafka_2.12-2.3.0-javadoc.jar
/usr/share/apache-kafka/libs/kafka_2.12-2.3.0-scaladoc.jar
/usr/share/apache-kafka/libs/kafka_2.12-2.3.0-sources.jar
/usr/share/apache-kafka/libs/kafka_2.12-2.3.0-test-sources.jar
/usr/share/apache-kafka/libs/kafka_2.12-2.3.0-test.jar
/usr/share/apache-kafka/libs/kafka_2.12-2.3.0.jar
/usr/share/apache-kafka/libs/log4j-1.2.17.jar
/usr/share/apache-kafka/libs/lz4-java-1.6.0.jar
/usr/share/apache-kafka/libs/maven-artifact-3.6.1.jar
/usr/share/apache-kafka/libs/metrics-core-2.2.0.jar
/usr/share/apache-kafka/libs/osgi-resource-locator-1.0.1.jar
/usr/share/apache-kafka/libs/paranamer-2.8.jar
/usr/share/apache-kafka/libs/plexus-utils-3.2.0.jar
/usr/share/apache-kafka/libs/reflections-0.9.11.jar
/usr/share/apache-kafka/libs/rocksdbjni-5.18.3.jar
/usr/share/apache-kafka/libs/scala-library-2.12.8.jar
/usr/share/apache-kafka/libs/scala-logging_2.12-3.9.0.jar
/usr/share/apache-kafka/libs/scala-reflect-2.12.8.jar
/usr/share/apache-kafka/libs/slf4j-api-1.7.26.jar
/usr/share/apache-kafka/libs/slf4j-log4j12-1.7.26.jar
/usr/share/apache-kafka/libs/snappy-java-1.1.7.3.jar
/usr/share/apache-kafka/libs/spotbugs-annotations-3.1.9.jar
/usr/share/apache-kafka/libs/validation-api-2.0.1.Final.jar
/usr/share/apache-kafka/libs/zkclient-0.11.jar
/usr/share/apache-kafka/libs/zookeeper-3.4.14.jar
/usr/share/apache-kafka/libs/zstd-jni-1.4.0-1.jar
/usr/share/apache-kafka/site-docs/kafka_2.12-2.3.0-site-docs.tgz
/usr/share/defaults/kafka/connect-console-sink.properties
/usr/share/defaults/kafka/connect-console-source.properties
/usr/share/defaults/kafka/connect-distributed.properties
/usr/share/defaults/kafka/connect-file-sink.properties
/usr/share/defaults/kafka/connect-file-source.properties
/usr/share/defaults/kafka/connect-log4j.properties
/usr/share/defaults/kafka/connect-standalone.properties
/usr/share/defaults/kafka/consumer.properties
/usr/share/defaults/kafka/log4j.properties
/usr/share/defaults/kafka/producer.properties
/usr/share/defaults/kafka/server.properties
/usr/share/defaults/kafka/tools-log4j.properties
/usr/share/defaults/kafka/trogdor.conf
/usr/share/defaults/kafka/zookeeper.properties

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/apache-kafka/LICENSE
/usr/share/package-licenses/apache-kafka/NOTICE

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/apache-kafka.service
