from Cli.cli import CLI
#from Cli.actions.redis_manager import RedisManager
import redis

def main():
    CLI().execute()
    r = r = redis.Redis(host='localhost', port=6379, decode_responses=True)

if __name__ == "__main__":
    main()