# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%bcond_without fedora

%define gcj_support 0
%define bootstrap 0

# If you don't want the -extras subpackage to be built
# in order to avoid its (Build)Requires
# give rpmbuild option '--without extra'

%define with_extra 0

%define section     free
%define jettyname   jetty
%define jtuid       110
%define username    %{name}
%define confdir     %{_sysconfdir}/%{name}
%define logdir      %{_logdir}/%{name}
%define homedir     %{_datadir}/%{name}
%define tempdir     %{_localstatedir}/cache/%{name}/temp
%define rundir      %{_localstatedir}/run/%{name}
%define libdir      %{_localstatedir}/lib/%{name}/lib
%define appdir      %{_localstatedir}/lib/%{name}/webapps
%define demodir     %{_localstatedir}/lib/%{name}/demo

Name:           jetty5
Version:        5.1.15
Release:        1.5.7
Epoch:          0
Summary:        The Jetty Webserver and Servlet Container

Group:          Development/Java
License:        Apache License
URL:            https://jetty.mortbay.org/jetty/
# Following source tarball was originally taken from the following location:
# http://www.ibiblio.org/maven/jetty/jetty-5.1.x/jetty-5.1.14.tgz
# The tarball was modified by removing all jars and BCLA licenses.
# tar -xzf jetty-5.1.14.tgz
# pushd jetty-5.1.14
# find . -name *.jar -exec rm {} \;
# rm ./etc/LICENSE.javax.xml.html ./etc/LICENSE.jsse.txt
# popd
# tar -czf jetty-5.1.14.fedora.tgz jetty-5.1.14/*
Source0:        %{jettyname}-%{version}.fedora.tgz
Source1:        jetty5.script
Source2:        jetty5.init
Source3:        jetty.logrotate
Source4:        jetty-OSGi-MANIFEST.MF
Patch0:         jetty-extra-j2ee-build_xml.patch
Patch1:         jetty-PostFileFilter.patch
Patch2:         jetty-libgcj-bad-serialization.patch
Patch3:         jetty-TestRFC2616-libgcj-bad-date-parser.patch
Patch4:		jetty-webdefault.patch
Patch5:		jetty-unix.patch


%if ! %{gcj_support}
BuildArch:      noarch
%endif

BuildRequires:  java-rpmbuild >= 0:1.6
#BuildRequires:  perl >= 0:5.005
# build only
BuildRequires:  ant-junit
BuildRequires:  jakarta-commons-collections
BuildRequires:  junit
BuildRequires:  xdoclet
BuildRequires:  xjavadoc
BuildRequires:  locales-en
# main
BuildRequires:  ant >= 0:1.6
BuildRequires:  jakarta-commons-el
BuildRequires:  jakarta-commons-logging
BuildRequires:  jsse
BuildRequires:  mx4j >= 0:3.0
BuildRequires:  tomcat5-jasper
BuildRequires:  jsp
BuildRequires:  tomcat5-servlet-2.4-api
BuildRequires:  xerces-j2 >= 0:2.7
BuildRequires:  xml-commons-apis
BuildRequires:  zip
BuildRequires:  tomcat5-webapps
# extra
%if %{with_extra}
BuildRequires:  carol
BuildRequires:  geronimo-j2ee-connector-1.5-api
BuildRequires:  geronimo-j2ee-management-1.0-api
BuildRequires:  howl-logger
BuildRequires:  hsqldb
BuildRequires:  jaf
BuildRequires:  jakarta-commons-cli
BuildRequires:  javamail
BuildRequires:  jboss4-cluster
BuildRequires:  jboss4-common
BuildRequires:  jboss4-j2ee
BuildRequires:  jboss4-jmx
BuildRequires:  jboss4-security
BuildRequires:  jboss4-server
BuildRequires:  jboss4-system
BuildRequires:  jgroups
BuildRequires:  jotm
BuildRequires:  geronimo-jta-1.0.1B-api
BuildRequires:  log4j
BuildRequires:  openorb-ots
BuildRequires:  xapool
%endif
#
Requires:  chkconfig
Requires:  jpackage-utils >= 0:1.6
Requires:  ant >= 0:1.6
Requires:  jakarta-commons-el
Requires:  jakarta-commons-logging
Requires:  tomcat5-jasper
Requires:  jsse
Requires:  mx4j >= 0:3.0
Requires:  tomcat5-servlet-2.4-api
Requires:  xerces-j2 >= 0:2.7
Requires:  xml-commons-apis

%if %{gcj_support}
BuildRequires:    java-gcj-compat-devel
%endif
Requires(pre):  rpm-helper
Requires(post):  rpm-helper
Requires(preun):  rpm-helper

%description
Jetty is a 100% Java HTTP Server and Servlet Container. 
This means that you do not need to configure and run a 
separate web server (like Apache) in order to use java, 
servlets and JSPs to generate dynamic content. Jetty is 
a fully featured web server for static and dynamic content. 
Unlike separate server/container solutions, this means 
that your web server and web application run in the same 
process, without interconnection overheads and complications. 
Furthermore, as a pure java component, Jetty can be simply 
included in your application for demonstration, distribution 
or deployment. Jetty is available on all Java supported 
platforms.  

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java

%description    javadoc
%{summary}.

%package        demo
Summary:        Examples for %{name}
Group:          Development/Java
Requires:       %{name} = 0:%{version}

%description    demo
%{summary}.

%if %{with_extra}
%package        extra
Summary:        Extras for %{name}
Group:          Development/Java
Requires:       %{name} = 0:%{version}
Requires:  carol
Requires:  geronimo-j2ee-connector-1.5-api
Requires:  geronimo-j2ee-management-1.0-api
Requires:  howl-logger
Requires:  hsqldb
Requires:  jaf
Requires:  jakarta-commons-cli
Requires:  javamail
Requires:  jboss4-cluster
Requires:  jboss4-common
Requires:  jboss4-j2ee
Requires:  jboss4-jmx
Requires:  jboss4-system
Requires:  jboss4-security
Requires:  jboss4-server
Requires:  jgroups
# jonas_timer
# objectweb-datasource
Requires:  jotm
Requires:  geronimo-jta-1.0.1B-api
Requires:  log4j
Requires:  openorb-ots
Requires:  xapool
Requires:  xdoclet
Requires:  xjavadoc

%description    extra
The purpose of this project is to enrich Jetty by 
selectively incorporating useful J2EE and non-J2EE 
features. The result is JettyPlus, an environment 
offering additional facilities to core web and servlet 
services, but which does not entail a full-blown 
application server (such as JettyJBoss and JettyJOnAS). 
The feature set currently contains: 
Java Transaction API (JTA) and Resource references, eg DataSources 
Java Naming and Directory Interface API (JNDI) 
Log4J 
Java Authentication and Authorization Service (JAAS) 
Java Mail  
These features have been implemented as a pluggable, 
Service-based architecture. This means that it is 
possible to develop and use alternative services to 
those provided. 
%endif

%package        manual
Summary:        Documents for %{name}
Group:          Development/Java
Requires:       %{name} = 0:%{version}

%description    manual
%{summary}.

%prep
%setup -q -n %{jettyname}-%{version}
mv demo/webapps/servlets-examples.war \
  demo/webapps/servlets-examples-dontdelete
mv demo/webapps/jsp-examples.war \
  demo/webapps/jsp-examples-dontdelete
for f in $(find . -name "*.?ar"); do rm $f; done
find . -name "*.class" -exec rm {} \;
# .war files needed for tests
mv demo/webapps/servlets-examples-dontdelete \
  demo/webapps/servlets-examples.war
mv demo/webapps/jsp-examples-dontdelete \
  demo/webapps/jsp-examples.war

%if %{bootstrap}
rm src/org/mortbay/util/jmx/MX4JHttpAdaptor.java
%endif

%patch0 -p0 -b .sav
%patch1 -p0 -b .sav
%patch2 -p0 -b .sav
%patch3 -p0 -b .sav
%patch4
%patch5

# Delete this Sun specific file.
rm src/org/mortbay/http/SunJsseListener.java

# Convert line endings...
%{__sed} -i 's/\r//' demo/webapps/jetty/auth/logon.html
%{__sed} -i 's/\r//' demo/webapps/jetty/auth/logon.jsp
%{__sed} -i 's/\r//' demo/webapps/jetty/auth/logonError.html

%build
export LC_ALL=ISO-8859-1

pushd ext
  ln -s $(build-classpath ant) .
  ln -s $(build-classpath commons-el) .
  ln -s $(build-classpath commons-logging) .
  ln -s $(build-classpath jasper5-compiler) jasper-compiler.jar
  ln -s $(build-classpath jasper5-runtime)  jasper-runtime.jar
  ln -s $(build-classpath mx4j/mx4j) .
  ln -s $(build-classpath mx4j/mx4j-jmx) .
  ln -s $(build-classpath mx4j/mx4j-remote) .
  ln -s $(build-classpath mx4j/mx4j-tools) .
  ln -s $(build-classpath xerces-j2) xercesImpl.jar
  ln -s $(build-classpath xml-commons-apis) xml-apis.jar
popd
%if %{with_extra}
pushd extra/ext
  ln -s $(build-classpath jaf) activation.jar
  ln -s $(build-classpath commons-cli) .
  ln -s $(build-classpath geronimo-j2ee-connector-1.5-api) connector-1_5.jar
  ln -s $(build-classpath hsqldb) .
  ln -s $(build-classpath geronimo-j2ee-management-1.0-api) javax77.jar
  ln -s $(build-classpath geronimo-jta-1.0.1B-api) jta-spec1_0_1.jar
  ln -s $(build-classpath log4j) .
  ln -s $(build-classpath javamail/mailapi) mail.jar
  ln -s $(build-classpath carol/ow_carol) .
  ln -s $(build-classpath howl-logger) .
#  #jonas_timer.jar
  ln -s $(build-classpath jotm/jotm) .
  ln -s $(build-classpath jotm/iiop-stubs) jotm_iiop_stubs.jar
  ln -s $(build-classpath jotm/jrmp-stubs) jotm_jrmp_stubs.jar
  ln -s $(build-classpath openorb-ots) jts1_0.jar
  #objectweb-datasource.jar
  ln -s $(build-classpath xapool) .
popd
%endif

export CLASSPATH=$(build-classpath \
xjavadoc \
)

%if %{with_extra}
CLASSPATH=$CLASSPATH:$(build-classpath \
jboss4/jboss-j2ee \
jboss4/jboss-common \
jboss4/jboss-system \
jboss4/jboss-jmx \
jboss4/jboss \
jboss4/jbosssx \
jboss4/jbossha \
jgroups \
log4j \
)
%endif

%if %{with_extra}
%{ant} -Dxdoclet.home=%{_javadir}/xdoclet -Dbuild.sysclasspath=first all extra
%else
%{ant} -Dxdoclet.home=%{_javadir}/xdoclet -Dbuild.sysclasspath=first all
%endif

# inject OSGi manifests
mkdir -p META-INF
cp %{SOURCE4} META-INF/MANIFEST.MF
zip -u lib/org.mortbay.jetty.jar META-INF/MANIFEST.MF

%install
rm -rf $RPM_BUILD_ROOT
# dirs
install -dm 755 $RPM_BUILD_ROOT%{_bindir}
install -dm 755 $RPM_BUILD_ROOT%{_initrddir}
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -dm 755 $RPM_BUILD_ROOT%{confdir}
install -dm 755 $RPM_BUILD_ROOT%{confdir}/extra
install -dm 755 $RPM_BUILD_ROOT%{demodir}
install -dm 755 $RPM_BUILD_ROOT%{homedir}
install -dm 755 $RPM_BUILD_ROOT%{homedir}/bin
install -dm 755 $RPM_BUILD_ROOT%{homedir}/ext
install -dm 755 $RPM_BUILD_ROOT%{homedir}/extra
install -dm 755 $RPM_BUILD_ROOT%{homedir}/extra/ext
install -dm 755 $RPM_BUILD_ROOT%{libdir}
install -dm 755 $RPM_BUILD_ROOT%{libdir}/extra
install -dm 755 $RPM_BUILD_ROOT%{logdir}
install -dm 755 $RPM_BUILD_ROOT%{rundir}
install -dm 755 $RPM_BUILD_ROOT%{tempdir}
install -dm 755 $RPM_BUILD_ROOT%{appdir}
# main pkg
install -pm 755 extra/unix/bin/jetty.sh $RPM_BUILD_ROOT%{_bindir}/d%{name}
install -pm 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -pm 755 %{SOURCE2} $RPM_BUILD_ROOT%{_initrddir}/%{name}
install -pm 644 start.jar $RPM_BUILD_ROOT%{homedir}/bin
install -pm 644 stop.jar $RPM_BUILD_ROOT%{homedir}/bin
cp -pr etc/* $RPM_BUILD_ROOT%{confdir}
touch $RPM_BUILD_ROOT%{confdir}/jetty.conf
install -pm 644 lib/org.mortbay.jetty.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-%{version}.jar
install -pm 644 lib/org.mortbay.jmx.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jmx-%{version}.jar
install -pm 644 lib/javax.servlet.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-servlet-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
pushd $RPM_BUILD_ROOT%{libdir}
  ln -sf %{_javadir}/%{name}/%{name}.jar org.mortbay.jetty.jar
  ln -sf %{_javadir}/%{name}/%{name}-jmx.jar org.mortbay.jmx.jar
popd
pushd $RPM_BUILD_ROOT%{homedir}/ext
ln -s $(build-classpath ant)
ln -s $(build-classpath jasper5-compiler)
ln -s $(build-classpath jasper5-runtime)
ln -s $(build-classpath commons-el)
ln -s $(build-classpath commons-logging)
ln -s $(build-classpath mx4j/mx4j-jmx)
ln -s $(build-classpath mx4j/mx4j-tools)
ln -s $(build-classpath servletapi5)
ln -s $(build-classpath jspapi)
ln -s $(build-classpath xerces-j2)
ln -s $(build-classpath xml-commons-apis)
popd
( cat << EO_RC
JAVA_HOME=/usr/lib/jvm/java
JAVA_OPTIONS=
JETTY_HOME=%{homedir}
JETTY_CONSOLE=%{logdir}/jetty-console.log
JETTY_PORT=8080
JETTY_RUN=%{_localstatedir}/run/%{name}
JETTY_PID=\$JETTY_RUN/jetty5.pid
EO_RC
) > $RPM_BUILD_ROOT%{homedir}/.jettyrc

# extra
%if %{with_extra}
cp -pr extra/etc/* $RPM_BUILD_ROOT%{confdir}/extra
rm $RPM_BUILD_ROOT%{confdir}/extra/LICENSE.apache.txt
rm $RPM_BUILD_ROOT%{confdir}/extra/LICENSE.hsqldb.html
rm $RPM_BUILD_ROOT%{confdir}/extra/LICENSE.p6spy.html

install -pm 644 extra/lib/org.jboss.jetty.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jboss-%{version}.jar
install -pm 644 extra/lib/org.mortbay.ftp.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-ftp-%{version}.jar
install -pm 644 extra/lib/org.mortbay.j2ee.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-j2ee-%{version}.jar
install -pm 644 extra/lib/org.mortbay.jaas.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jaas-%{version}.jar
install -pm 644 extra/lib/org.mortbay.jsr77.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jsr77-%{version}.jar
# omit for 1.6
# install -pm 644 extra/lib/org.mortbay.jetty-jdk1.2.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jetty-jdk1.2-%{version}.jar
install -pm 644 extra/lib/org.mortbay.jetty.plus.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-plus-%{version}.jar
# omit for 1.6
# install -pm 644 extra/lib/org.mortbay.jmx-jdk1.2.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jmx-jdk1.2-%{version}.jar
install -pm 644 extra/lib/org.mortbay.loadbalancer.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-loadbalancer-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
pushd $RPM_BUILD_ROOT%{libdir}/extra
  ln -sf %{_javadir}/%{name}/%{name}-jboss.jar org.jboss.jetty.jar
  ln -sf %{_javadir}/%{name}/%{name}-ftp.jar org.mortbay.ftp.jar
  ln -sf %{_javadir}/%{name}/%{name}-j2ee.jar org.mortbay.j2ee.jar
  ln -sf %{_javadir}/%{name}/%{name}-jaas.jar org.mortbay.jaas.jar
  ln -sf %{_javadir}/%{name}/%{name}-jsr77.jar org.mortbay.jsr77.jar
  ln -sf %{_javadir}/%{name}/%{name}-plus.jar org.mortbay.jetty.plus.jar
  ln -sf %{_javadir}/%{name}/%{name}-loadbalancer.jar org.mortbay.loadbalancer.jar
popd
pushd $RPM_BUILD_ROOT%{homedir}/extra/ext
  #jonas_timer.jar
  #objectweb-datasource.jar
ln -s $(build-classpath jaf)
ln -s $(build-classpath carol/carol)
ln -s $(build-classpath commons-cli)
ln -s $(build-classpath hsqldb)
ln -s $(build-classpath jotm/jotm)
ln -s $(build-classpath jotm/iiop-stubs)
ln -s $(build-classpath jotm/jrmp-stubs)
ln -s $(build-classpath jta)
ln -s $(build-classpath openorb-ots)
ln -s $(build-classpath log4j)
ln -s $(build-classpath javamail/mailapi)
ln -s $(build-classpath xapool)
popd
%endif

# demo
cp -pr demo/* $RPM_BUILD_ROOT%{demodir}

# javadoc
cp -pr webapps/* $RPM_BUILD_ROOT%{appdir}
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
pushd $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
unzip -q $RPM_BUILD_ROOT%{appdir}/javadoc.war
popd
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# manual
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p {LICENSE.TXT,VERSION.TXT} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
mv $RPM_BUILD_ROOT%{demodir}/webapps/jetty/* \
                $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm -rf $RPM_BUILD_ROOT%{appdir}/jetty

pushd $RPM_BUILD_ROOT%{homedir}
   [ -d etc ]    || ln -fs %{confdir}   etc
   [ -d demo ]    || ln -fs %{demodir}   demo
   [ -d logs ]    || ln -fs %{logdir}    logs
   [ -d lib ]     || ln -fs %{libdir}    lib
   [ -d temp ]    || ln -fs %{tempdir}   temp
   [ -d webapps ] || ln -fs %{appdir}    webapps
%if %{with_extra}
   pushd extra
     [ -d etc ]    || ln -fs %{confdir}/extra  etc
     [ -d lib ]    || ln -fs %{libdir}/extra    lib
   popd
%endif
popd

# no need to fix paths
#perl -pi -e 's#etc/#conf/#g;' $RPM_BUILD_ROOT%{confdir}/*.xml

(cd %{buildroot} && ln -s %{_javadocdir}/%{name} ./%{homedir}/javadoc)

(cd %{buildroot} && ln -s %{_docdir}/%{name}-%{version} ./%{demodir}/webapps/jetty)

%if %{gcj_support}
%{_bindir}/aot-compile-rpm \
    --exclude %{_docdir}/%{name}-%{version}/WEB-INF/classes \
    --exclude %{_localstatedir}/lib/jetty5/webapps/template/WEB-INF/classes
%if 0
    --exclude %{_localstatedir}/lib/jetty5/demo/webapps/servlets-examples.war \
    --exclude %{_localstatedir}/lib/jetty5/demo/webapps/jsp-examples.war
%endif
%endif

%pre
# Add the "jetty5" user and group
# we need a shell to be able to use su - later
%_pre_useradd %{name} %{homedir} /bin/sh
%_pre_groupadd %{name} %{name}
#%{_sbindir}/groupadd -g %{jtuid} %{name} 2> /dev/null || :
#%{_sbindir}/useradd -c "Jetty5" -u %{jtuid} -g %{name} \
#    -s /bin/sh -d %{homedir} %{name} 2> /dev/null || :

%post
%_post_service %{name}
%if %{gcj_support}
%{update_gcjdb}
%endif

%if %{gcj_support}
%postun
%{clean_gcjdb}
%endif

%preun
%_preun_service %{name}
if [ $1 = 0 ]; then
# Don't
#   %{_sbindir}/userdel %{name} >> /dev/null 2>&1 || :
#   %{_sbindir}/groupdel %{name} >> /dev/null 2>&1 || :

    # Remove automated symlinks
    for repository in %{homedir}/ext ; do
        find $repository -name '\[*\]*.jar' ! -type d -exec rm -f {} \;
    done
fi

%if %{with_extra}
%preun extra
  for repository in %{homedir}/extra/ext ; do
      find $repository -name '\[*\]*.jar' ! -type d -exec rm -f {} \;
  done
%endif

%files
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/*
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}-%{version}.jar
%{_javadir}/%{name}/%{name}-jmx-%{version}.jar
%{_javadir}/%{name}/%{name}-servlet-%{version}.jar
%{_javadir}/%{name}/%{name}.jar
%{_javadir}/%{name}/%{name}-jmx.jar
%{_javadir}/%{name}/%{name}-servlet.jar
%config(noreplace) %{confdir}
%dir %{libdir}
%{libdir}/org.mortbay.jetty.jar
%{libdir}/org.mortbay.jmx.jar
%dir %{homedir}
%{homedir}/[^e]*
%{homedir}/ext
%{homedir}/etc
%{homedir}/.jettyrc
%dir %{demodir}
%attr(755, jetty5, jetty5) %{logdir}
%attr(755, jetty5, jetty5) %{tempdir}
%attr(755, jetty5, jetty5) %{rundir}
%dir %{appdir}
%attr(0755,root,root) %{_initrddir}/%{name}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-jmx-%{version}.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-servlet-%{version}.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/start.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/stop.jar.*
%endif

%files demo
%defattr(-,root,root,0755)
%{demodir}

%files javadoc
%defattr(0644,root,root,0755)
%{appdir}/template
%{appdir}/javadoc.war
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%defattr(0644,root,root,0755)
%doc %{_docdir}/%{name}-%{version}

%if %{with_extra}
%files extra
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-ftp-%{version}.jar
%{_javadir}/%{name}/%{name}-ftp.jar
%{_javadir}/%{name}/%{name}-j2ee-%{version}.jar
%{_javadir}/%{name}/%{name}-j2ee.jar
%{_javadir}/%{name}/%{name}-jaas-%{version}.jar
%{_javadir}/%{name}/%{name}-jaas.jar
%{_javadir}/%{name}/%{name}-jboss-%{version}.jar
%{_javadir}/%{name}/%{name}-jboss.jar
%{_javadir}/%{name}/%{name}-jsr77-%{version}.jar
%{_javadir}/%{name}/%{name}-jsr77.jar
%{_javadir}/%{name}/%{name}-loadbalancer-%{version}.jar
%{_javadir}/%{name}/%{name}-loadbalancer.jar
%{_javadir}/%{name}/%{name}-plus-%{version}.jar
%{_javadir}/%{name}/%{name}-plus.jar
%{confdir}/extra
%{homedir}/extra
%{libdir}/extra
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-ftp-%{version}.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-j2ee-%{version}.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-jaas-%{version}.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-jboss-%{version}.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-jsr77-%{version}.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-loadbalancer-%{version}.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-plus-%{version}.jar.*
%endif
%endif


%changelog
* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0:5.1.15-1.5.4mdv2011.0
+ Revision: 606080
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0:5.1.15-1.5.3mdv2010.1
+ Revision: 523082
- rebuilt for 2010.1

* Thu Oct 29 2009 Oden Eriksson <oeriksson@mandriva.com> 0:5.1.15-1.5.2mdv2010.0
+ Revision: 460086
- more fixes in the initscript

* Thu Oct 29 2009 Anne Nicolas <ennael@mandriva.org> 0:5.1.15-1.5.1mdv2010.0
+ Revision: 459956
- fix initscript (#53952)

* Tue Oct 27 2009 Oden Eriksson <oeriksson@mandriva.com> 0:5.1.15-1.5.0mdv2010.0
+ Revision: 459587
- sync with fc11

* Tue Oct 27 2009 Anne Nicolas <ennael@mandriva.org> 0:5.1.14-1.5.4mdv2010.0
+ Revision: 459570
- fix build
- fix functions not sourced
  fix LSB compliance for init script (#53952)

  + Christophe Fergeau <cfergeau@mandriva.com>
    - rebuild

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Thu Jul 31 2008 Alexander Kurtakov <akurtakov@mandriva.org> 0:5.1.14-1.5.1mdv2009.0
+ Revision: 257688
- update OSGi manifest

* Mon Jul 07 2008 Alexander Kurtakov <akurtakov@mandriva.org> 0:5.1.14-1.2.1mdv2009.0
+ Revision: 232322
- new version 5.1.14 \ sync with fedora

* Tue Mar 04 2008 Alexander Kurtakov <akurtakov@mandriva.org> 0:5.1.12-1.0.7mdv2008.1
+ Revision: 179023
- add zip BR

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Anssi Hannula <anssi@mandriva.org>
    - buildrequire java-rpmbuild, i.e. build with icedtea on x86(_64)

* Sat Sep 15 2007 Anssi Hannula <anssi@mandriva.org> 0:5.1.12-1.0.5mdv2008.0
+ Revision: 87432
- rebuild to filter out autorequires of GCJ AOT objects
- remove unnecessary Requires(post) on java-gcj-compat

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 0:5.1.12-1.0.4mdv2008.0
+ Revision: 70277
- kill file require on chkconfig

* Sat Aug 04 2007 David Walluck <walluck@mandriva.org> 0:5.1.12-1.0.3mdv2008.0
+ Revision: 58979
- add eclipse manifest

* Fri Jul 27 2007 David Walluck <walluck@mandriva.org> 0:5.1.12-1.0.1mdv2008.0
+ Revision: 56273
- fix jsp BuildRequires
- BuildRequires: tomcat5-jsp
- Import jetty5



* Fri Feb 02 2007 Ralph Apel <r.apel at r-apel.de> - 0:5.1.12-1jpp
- Upgrade to 5.1.12
- Add gcj_support option
- Avoid circular dependency with mx4j-tools thru bootstrap option

* Thu Aug 10 2006 Ralph Apel <r.apel@r-apel.de> - 0:5.1.11-0.rc0.2jpp
- Fix version/release in changelog
- Introduce option '--without extra' to omit this subpackage and its (B)Rs
- Don't delete user on erase
- Tidy up BRs
- Add commons-el.jar to ext
- No ghost for lib/org.mortbay.jetty.jar, lib/org.mortbay.jmx.jar
- Avoid use of build-jar-repository in spec
- Avoid use of rebuild-jar-repository in init and start script
- Don't handle JETTY_PID file in init script: start script takes care
- Patch PostFileFilter to remove a (unused) com.sun package import
- Explicitly (B)R  geronimo-jta-1.0.1B-api instead of any jta
- Add empty file /etc/jetty5/jetty.conf: 
  activate contexts manually if desired

* Tue Jun 20 2006 Ralph Apel <r.apel@r-apel.de> - 0:5.1.2-3jpp
- First JPP-1.7 release

* Mon Mar 14 2005 Ralph Apel <r.apel@r-apel.de> - 0:5.1.2-2jpp
- link commons-logging to %%{_homedir}/ext
- link jspapi to %%{_homedir}/ext
- only use %%{_homedir}/etc not conf

* Tue Feb 01 2005 Ralph Apel <r.apel@r-apel.de> - 0:5.1.2-1jpp
- Upgrade to 5.1.2
- Prepare for build with Java 1.5, (thx to Petr Adamek)
- Require /sbin/chkconfig instead of chkconfig package

* Tue Jan 04 2005 Ralph Apel <r.apel@r-apel.de> - 0:5.0.0-2jpp
- Include build of extra, so called JettyPlus
- Create own subdirectory for jetty5 in %%{_javadir}
- Change %%{_homedir}/conf to %%{_homedir}/etc
- Dropped chkconfig requirement; just exec if /sbin/chkconfig available
- Fixed unpackaged .jettyrc

* Mon Oct 04 2004 Ralph Apel <r.apel@r-apel.de> - 0:5.0.0-1jpp
- Upgrade to 5.0.0
- Fixed URL
- relaxed some versioned dependencies

* Sun Aug 23 2004 Randy Watler <rwatler at finali.com> - 0:4.2.20-2jpp
- Rebuild with ant-1.6.2

* Fri Jun 18 2004 Ralph Apel <r.apel@r-apel.de> - 0:4.2.20-1jpp
- Upgrade to 4.2.20
- Drop ownership of /usr/share/java and /usr/bin

* Tue Feb 24 2004 Ralph Apel <r.apel@r-apel.de> - 0:4.2.17-2jpp
- enhancements and corrections thanks to Kaj J. Niemi:
- $JETTY_HOME/ext didn't exist but %%post depended on it
- correctly shutdown jetty upon uninstall
- RedHat depends on chkconfig/service to work so a functional
  init.d/jetty4 needed to be created
- djetty4 (jetty.sh) did funny things especially when it attempted to guess
  stuff
- a lot of .xml config files assumed that the configs were in etc/ instead of
  conf/

* Thu Feb 19 2004 Ralph Apel <r.apel@r-apel.de> - 0:4.2.17-1jpp
- First JPackage release.
