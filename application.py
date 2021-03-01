import ldclient
from ldclient.config import Config

if __name__ == "__main__":
  sdk_key = "sdk-eb9b8342-2cc9-4b80-920d-fdbcd63df7e2"
  ldclient.set_config(Config(sdk_key))


user = {
  "key": "1",
  "firstName": "Moshin",
  "lastName": "Jaffar",
  "custom": {
    "groups": "beta_testers"
  }
}

show_feature = ldclient.get().variation("logging-features", user, False)

if show_feature:
# application code to show the feature
  print("Showing your feature")
else:
# the code to run if the feature is off
  print("Not showing your feature")

# shut down the client, since we're about to quit
ld_client.close()

