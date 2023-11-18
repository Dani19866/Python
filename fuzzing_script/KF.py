<<<<<<< HEAD
import CLI.CLIKrakenFuzz as CLI
import ClassKrakenFuzz.init as INIT

if __name__ == "__main__":
    try:
        args = CLI.cli()
        INIT.runKraken(args)
        
    except KeyboardInterrupt:
        print( "[-] Exiting..." )
        exit(1)
=======
import CLI.CLIKrakenFuzz as CLI
import ClassKrakenFuzz.init as INIT

if __name__ == "__main__":
    try:
        args = CLI.cli()
        INIT.runKraken(args)
        
    except KeyboardInterrupt:
        print( "[-] Exiting..." )
        exit(1)
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
