EventBridge
-----------

This talk was written for Serverless London in Feb 2020.

Slides are rendered with the [1-2-3 remark theme][1] and contain diagrams rendered with [Mingrammer's "diagrams" library][2].

To serve the slides, run a webserver rooted at the top level directory, eg. if the talk is checked out to /tmp/foo then

```sh
cd /tmp/foo
python -m http.server
echo "slides available on localhost:8000"
```
To generate the slides, you'll need to install `diagrams` per the instructions paying particular attention to the version of Graphviz.

Handily, the `make` command will generate diagrams and start a server for you.

[1]: https://1-2-3.github.io/remark-it/index-en_US.html
[2]: https://diagrams.mingrammer.com/
