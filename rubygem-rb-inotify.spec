#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-rb-inotify
Version  : 0.9.5
Release  : 2
URL      : https://rubygems.org/downloads/rb-inotify-0.9.5.gem
Source0  : https://rubygems.org/downloads/rb-inotify-0.9.5.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-ffi
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-yard

%description
# rb-inotify
This is a simple wrapper over the [inotify](http://en.wikipedia.org/wiki/Inotify) Linux kernel subsystem
for monitoring changes to files and directories.
It uses the [FFI](http://wiki.github.com/ffi/ffi) gem to avoid having to compile a C extension.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n rb-inotify-0.9.5
gem spec %{SOURCE0} -l --ruby > rubygem-rb-inotify.gemspec

%build
gem build rubygem-rb-inotify.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
rb-inotify-0.9.5.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/rb-inotify-0.9.5.gem
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Event/absolute_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Event/callback%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Event/cdesc-Event.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Event/consume-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Event/cookie-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Event/fix_encoding-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Event/flags-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Event/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Event/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Event/notifier-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Event/related-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Event/size-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Event/watcher-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Event/watcher_id-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Native/Event/cdesc-Event.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Native/FFI/Library/cdesc-Library.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Native/FFI/cdesc-FFI.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Native/Flags/cdesc-Flags.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Native/Flags/from_mask-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Native/Flags/to_mask-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Native/cdesc-Native.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Notifier/cdesc-Notifier.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Notifier/close-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Notifier/fd-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Notifier/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Notifier/process-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Notifier/read_events-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Notifier/readpartial-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Notifier/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Notifier/stop-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Notifier/supports_ruby_io%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Notifier/to_io-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Notifier/watch-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Notifier/watchers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Watcher/callback%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Watcher/cdesc-Watcher.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Watcher/close-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Watcher/flags-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Watcher/id-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Watcher/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Watcher/notifier-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/Watcher/path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/INotify/cdesc-INotify.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-inotify-0.9.5/ri/page-README_md.ri
/usr/lib64/ruby/gems/2.2.0/gems/rb-inotify-0.9.5/.yardopts
/usr/lib64/ruby/gems/2.2.0/gems/rb-inotify-0.9.5/MIT-LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/rb-inotify-0.9.5/README.md
/usr/lib64/ruby/gems/2.2.0/gems/rb-inotify-0.9.5/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/rb-inotify-0.9.5/VERSION
/usr/lib64/ruby/gems/2.2.0/gems/rb-inotify-0.9.5/lib/rb-inotify.rb
/usr/lib64/ruby/gems/2.2.0/gems/rb-inotify-0.9.5/lib/rb-inotify/event.rb
/usr/lib64/ruby/gems/2.2.0/gems/rb-inotify-0.9.5/lib/rb-inotify/native.rb
/usr/lib64/ruby/gems/2.2.0/gems/rb-inotify-0.9.5/lib/rb-inotify/native/flags.rb
/usr/lib64/ruby/gems/2.2.0/gems/rb-inotify-0.9.5/lib/rb-inotify/notifier.rb
/usr/lib64/ruby/gems/2.2.0/gems/rb-inotify-0.9.5/lib/rb-inotify/watcher.rb
/usr/lib64/ruby/gems/2.2.0/gems/rb-inotify-0.9.5/rb-inotify.gemspec
/usr/lib64/ruby/gems/2.2.0/specifications/rb-inotify-0.9.5.gemspec
