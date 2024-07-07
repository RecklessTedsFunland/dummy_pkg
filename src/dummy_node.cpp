#include <rclcpp/rclcpp.hpp>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

struct Params{
  string arg;
  string val;
};

vector<Params> handle_args(int argc, char ** argv) {
  vector<Params> args;
  for (int i=1; i<argc; ++i) {
    string s(argv[i]);
    if (s == "--ros-args") break;
    else if (s.find("--") == 0) {
      size_t loc = s.find('=');
      if (loc != string::npos) {
        string key = s.substr(2,loc-2);
        string val = s.substr(loc+1,s.size()-loc-1);
        Params p{key,val};
        args.push_back(p);
      }
      else {
        string key = s.substr(2,s.size()-2);
        string val = "";
        Params p{key,val};
        args.push_back(p);
      }
    }
  }
  return args;
}


int main(int argc, char ** argv) {
  (void) argc;
  (void) argv;

  rclcpp::init(argc, argv);

  printf("argc: %d\n", argc);
  for (int i=0; i<argc; ++i) printf("> %s\n", argv[i]);

  // printf("hello world dummy_pkg package\n");

  vector<Params> args = handle_args(argc, argv);
  for (const Params& p: args) {
    if (p.arg == "help") printf("==> Help\n");
    else if (p.arg == "frame") printf("==> Frame: %s\n", p.val.c_str());
    else if (p.arg == "name") printf("==> Name: %s\n", p.val.c_str());
    else printf("*** Ingored %s = %s\n", p.arg.c_str(), p.val.c_str());
  }

  rclcpp::shutdown();
  return 0;
}
