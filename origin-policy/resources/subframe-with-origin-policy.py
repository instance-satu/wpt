def main(request, response):
    """Send a response with the Origin-Policy header asking for the latest
      policy, that runs the test JS given by the ?test= argument. This is meant
       to be loaded into an iframe by origin-policy-test-runner.js.

       The ?test= argument is best given as an absolute path (starting with /)
       since it will otherwise be interpreted relative to where this file is
       served.
    """
    test_file = request.GET.first("test")

    response.headers.set("Origin-Policy", "allowed=(latest)")
    response.headers.set("Content-Type", "text/html")

    return """
    <!DOCTYPE html>
    <meta charset="utf-8">
    <title>Origin policy subframe</title>

    <script src="/resources/testharness.js"></script>
    <script src="/resources/testharnessreport.js"></script>

    <div id="log"></div>

    <script type="module" src="%s"></script>
  """ % test_file
