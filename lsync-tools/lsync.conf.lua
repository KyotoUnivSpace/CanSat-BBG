-- variables
local source = ".."
local target = "debian@192.168.6.2:sync/CanSat-BBG"
local homeDir = os.getenv("HOME")

-- lsyncd
settings {
  logfile     = "/tmp/lsyncd.log",
  statusFile  = "/tmp/lsyncd.status",
  insist      = true,
  nodaemon    = true,
  statusInterval  = 10,
  maxProcesses    = 2,
}

sync {
  default.rsync,
  delete = true,
  source = source,
  target = target,
  delay  = 1,
  exclude = {".DS_Store", ".vscode", "lsync-tools"},
  rsync = {
    binary = "/usr/local/bin/rsync",
    archive = true,
    compress = true,
    rsh = "/usr/bin/ssh -i "..homeDir.."/.ssh/id_rsa"
  }
}
