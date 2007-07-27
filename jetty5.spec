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

%define _with_gcj_support 1
%define gcj_support %{?_with_gcj_support:1}%{!?_with_gcj_support:%{?_without_gcj_support:0}%{!?_without_gcj_support:%{?_gcj_support:%{_gcj_support}}%{!?_gcj_support:0}}}
%define bootstrap %{?_with_bootstrap:1}%{!?_with_bootstrap:%{?_without_bootstrap:0}%{!?_without_bootstrap:%{?_bootstrap:%{_bootstrap}}%{!?_bootstrap:0}}}

# If you don't want the -extras subpackage to be built
# in order to avoid its (Build)Requires
# give rpmbuild option '--without extra'

%define _without_extra 1
%define without_extra %{?_without_extra:1}%{!?_without_extra:0}
%define with_extra %{!?_without_extra:1}%{?_without_extra:0}

%define _localstatedir %{_var}

%define section     free
%define jettyname   jetty
%define jtuid       110
%define confdir            %{_sysconfdir}/%{name}
%define logdir            %{_logdir}/%{name}
%define homedir            %{_datadir}/%{name}
%define tempdir            %{_localstatedir}/cache/%{name}/temp
%define rundir            %{_localstatedir}/run/%{name}
%define libdir            %{_localstatedir}/lib/%{name}/lib
%define appdir            %{_localstatedir}/lib/%{name}/webapps
%define demodir            %{_localstatedir}/lib/%{name}/demo

Name:           jetty5
Version:        5.1.12
Release:        %mkrel 1.0.1
Epoch:          0
Summary:        The Jetty Webserver and Servlet Container

Group:          Development/Java
License:        Apache License
URL:            http://jetty.mortbay.org/jetty/
Source0:        %{jettyname}-%{version}.zip
Source1:        jetty5.script
Source2:        jetty5.init
Patch0:                jetty5-extra-j2ee-build_xml.patch
Patch1:                jetty5-extra-jdk1.2-build_xml.patch
Patch2:                jetty5-PostFileFilter.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%if ! %{gcj_support}
BuildArch:      noarch
%endif

BuildRequires:  jpackage-utils >= 0:1.6
#BuildRequires:  perl >= 0:5.005
# build only
BuildRequires:  ant-junit
BuildRequires:  jakarta-commons-collections
BuildRequires:  junit
BuildRequires:  xdoclet
BuildRequires:  xjavadoc
# main
BuildRequires:  ant >= 0:1.6
BuildRequires:  jakarta-commons-el
BuildRequires:  jakarta-commons-logging
BuildRequires:  jsse
BuildRequires:  mx4j >= 0:3.0
BuildRequires:  tomcat5-jasper
BuildRequires:  tomcat5-servlet-2.4-api
BuildRequires:  xerces-j2 >= 0:2.7
BuildRequires:  xml-commons-apis

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
Requires:  /sbin/chkconfig
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
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat
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
Requires(post):   /bin/rm,/bin/ln
Requires(postun): /bin/rm

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
for f in $(find . -name "*.?ar"); do rm $f; done
find . -name "*.class" -exec rm {} \;
rm src/org/mortbay/http/SunJsseListener.java

%if %{bootstrap}
rm src/org/mortbay/util/jmx/MX4JHttpAdaptor.java
%endif

%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav

%{__perl} -pi -e 's/<javac(\s+|$)/<javac nowarn="true"\1/g' `%{_bindir}/find . -type f -name build.xml`

%{_bindir}/find . -name '*.txt' -print0 | %{_bindir}/xargs -0 -t %{__chmod} 0644
%{_bindir}/find . -name '*.sh' -print | %{_bindir}/xargs -t %{__chmod} 0755
%{_bindir}/find . -name '*.MF' -o -name '*.html' -o -name '*.jsp' | \
  %{_bindir}/xargs -t %{__perl} -pi -e 's/\r//g'

%build

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

%define all prepare jars webapps javadoc

%if %{with_extra}
%{ant} -Dxdoclet.home=%{_javadir}/xdoclet -Dbuild.sysclasspath=first %{all} extra
%else
%{ant} -Dxdoclet.home=%{_javadir}/xdoclet -Dbuild.sysclasspath=first %{all}
%endif

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

%clean
rm -rf $RPM_BUILD_ROOT

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
%doc %{_docdir}/%{name}-%{version}/LICENSE.TXT
%doc %{_docdir}/%{name}-%{version}/VERSION.TXT
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
