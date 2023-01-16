public class Clone888 {
/*
* Semantic clone benchmark
*  Source code are extracted from Stack Overflow
*  Stack overflow Question #:14617
*  Stack Overflow answer #:18975867
*  And Stack Overflow answer#:2404783
*/
public static void main (String [] args) {
    SendMy***Files*** sendMyFiles = new SendMy***Files*** ();
    if (args.length < 1) {
        System.err.println ("Usage: java " + sendMy***Files***.getClass ().getName () + " ***Properties_file File_To_FTP*** ");
        System.exit (1);
    }
    String ***propertiesFile*** = args [0].trim ();
    String ***fileToFTP*** = args [1].trim ();
    sendMyFiles.***startFTP*** (***propertiesFile***, ***fileToFTP***);
}

public static void main (String [] args) throws IOException {
    final SSHClient ssh = new SSHClient ();
    ssh.loadKnownHosts ();
    ssh.connect ("localhost");
    try {
        ssh.authPublickey (System.***getProperty*** ("user.name"));
        final String src = System.***getProperty*** ("user.home") + ***File***.separator + "test_file";
        final ***SFTPClient*** sftp = ssh.***newSFTPClient*** ();
        try {
            sftp.put (new ***FileSystemFile*** (src), "/tmp");
        } finally {
            ***sftp***.close ();
        }
    } finally {
        ssh.disconnect ();
    }
}

}
