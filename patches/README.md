# Patches

* [Chiliproject - Rubyish](https://github.com/chiliproject/chiliproject/compare/master...grumps:1369_port_rdm_mailhandler)
    ```
    @@ -65,8 +65,7 @@
     require 'net/http'
     require 'net/https'
     require 'uri'
    -require 'getoptlong'
    -require 'rdoc/usage'
    +require 'optparse'
     
     module Net
       class HTTPS < HTTP
     @@ -83,53 +82,49 @@ def self.post_form(url, params, headers)
     end
     
     class RedmineMailHandler
    +  VERSION = '0.1'
    *  VERSION = '0.2'
     
       attr_accessor :verbose, :issue_attributes, :allow_override, :unknown_user, :no_permission_check, :url, :key
    -
    *      @allow_override = []
       def initialize
    +
         self.issue_attributes = {}
     
    +    opts = GetoptLong.new(
    +      [ '--help',           '-h', GetoptLong::NO_ARGUMENT ],
    +      [ '--version',        '-V', GetoptLong::NO_ARGUMENT ],
    +      [ '--verbose',        '-v', GetoptLong::NO_ARGUMENT ],
    +      [ '--url',            '-u', GetoptLong::REQUIRED_ARGUMENT ],
    +      [ '--key',            '-k', GetoptLong::REQUIRED_ARGUMENT],
    +      [ '--project',        '-p', GetoptLong::REQUIRED_ARGUMENT ],
    +      [ '--status',         '-s', GetoptLong::REQUIRED_ARGUMENT ],
    +      [ '--tracker',        '-t', GetoptLong::REQUIRED_ARGUMENT],
    +      [ '--category',             GetoptLong::REQUIRED_ARGUMENT],
    +      [ '--priority',             GetoptLong::REQUIRED_ARGUMENT],
    +      [ '--allow-override', '-o', GetoptLong::REQUIRED_ARGUMENT],
    +      [ '--unknown-user',         GetoptLong::REQUIRED_ARGUMENT],
    +      [ '--no-permission-check',  GetoptLong::NO_ARGUMENT]
    +    )
    -
    +    opts.each do |opt, arg|
    +      case opt
    +      when '--url'
    +        self.url = arg.dup
    +      when '--key'
    +        self.key = arg.dup
    +      when '--help'
    +        usage
    +      when '--verbose'
    +        self.verbose = true
    +      when '--version'
    +        puts VERSION; exit
    +      when '--project', '--status', '--tracker', '--category', '--priority'
    +        self.issue_attributes[opt.gsub(%r{^\-\-}, '')] = arg.dup
    +      when '--allow-override'
    +        self.allow_override = arg.dup
    +      when '--unknown-user'
    +        self.unknown_user = arg.dup
    +      when '--no-permission-check'
    +        self.no_permission_check = '1'
    *    optparse = OptionParser.new do |opts|
    *      
    *      
    *      opts.banner = "rdm-mailhandler [options] --url=<Redmine URL> --key=<API key>"
    *      opts.separator("")
    *      opts.separator("Required arguments:")
    *      opts.on("-u", "--url URL",            "URL of the Redmine server") {|v| self.url = v}
    *      opts.on("-k", "--key KEY",            "Redmine API key") {|v| self.key = v}
    *      opts.separator("")
    *      opts.separator("Options:")
    *      opts.on("--unknown-user",             "how to handle emails from an unknown user",
    *                                            "ACTION can be one of the following values:",
    *                                            "ignore: email is ignored (default)",
    *                                            "accept: accept as anonymous user",
    *                                            "create: create a user account") {|v| self.unknown_user = v}
    *      opts.on("--no-permission-check",      "disable permission checking when receiving",
    *                                            "the email") {self.no_permission_check= '1'}
    *      opts.on("-v", "--verbose",            "verbose") {self.verbose = true}
    *      opts.on("-V", "--version",            "show version and exit") {puts VERSION; exit}
    *      opts.separator("")
    *      opts.separator("Issue attributes control options:")
    *      opts.on("-p", "--project PROJECT",    "identifier of the target project") {|v| self.project = v}
    *      opts.on("-s", "--status STATUS",      "name of the target status") {|v| self.status = v}
    *      opts.on("-t", "--tracker TRACKER",    "name of the target tracker") {|v| self.tracker = v}
    *      opts.on("--category CATEGORY",        "name of the target category") {|v| self.category = v}
    *      opts.on("--priority PRIORITY",        "name of the target priority") {|v| self.priority = v}
    *      opts.on("--allow-override OVERRIDE",  "allow email content to override attributes",
    *                                            "ATTRS is a comma separated list of attributes") {|v| self.allow_override = v}
    *      opts.on("-h", "--help",               "show help and exit") do
    *        puts opts
    *        exit 1
           end
         end
    *    optparse.parse!
     
    +    RDoc.usage if url.nil?
       end
     
       def submit(email)
     @@ -178,4 +173,4 @@ def debug(msg)
     end
     
     handler = RedmineMailHandler.new
    -exit(handler.submit(STDIN.read))
    +exit(handler.submit(STDIN.read)) 
    ```
