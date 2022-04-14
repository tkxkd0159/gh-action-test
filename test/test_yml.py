import unittest
import yaml
import os
from dotenv import load_dotenv
import requests

load_dotenv()


class TestYAML(unittest.TestCase):
    def test_change_kv(self):
        with open("test/test.yml") as f:
            tmp = yaml.load(f, yaml.Loader)
            tmp['image']['tag'] = "sha-11235"
        with open("test/test2.yml", "w") as f2:
            yaml.dump(tmp, f2)

        with open("test/test2.yml") as f2:
            new_yaml = yaml.load(f2, yaml.Loader)

        self.assertEqual(new_yaml['image']['tag'], "sha-11235")

    def test_get_yaml(self):
        repo = "https://raw.githubusercontent.com/Carina-labs/helm-charts"
        commit = "a69a7dc33168f540faef238b275d42e305fe8e62"
        target_file = f"{repo}/{commit}/testnet/novachain-node/values.yaml"
        user = "vvictorl"
        gh_pat = os.getenv("A41_PAT")
        r = requests.get(target_file, auth=(user, gh_pat))

        with open("test/test.yml") as f:
            self.assertEqual(yaml.load(f.read(), yaml.Loader), yaml.load(r.text, yaml.Loader))




if __name__ == '__main__':
    unittest.TestCase.maxDiff = None
    unittest.main()