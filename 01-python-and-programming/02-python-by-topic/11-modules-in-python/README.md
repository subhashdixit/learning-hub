# 11 — Modules in Python

[Python learning path](../../README.md) · [Open the notebook](examples.ipynb)

Read the notes and examples below, or open the notebook to run them. These are extracted from the existing Python notes; they have not been rewritten or executed during organization.

#11. Modules in Python

- math
- keywords
- random
- datetime

```python
# math
import math

math.sqrt(196)
```

```python
# keyword
import keyword
print(keyword.kwlist)
```

Recorded output:
```text
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

```python
# random
import random
print(random.randint(1,100))
```

Recorded output:
```text
53
```

```python
# datetime
import datetime
print(datetime.datetime.now())
```

Recorded output:
```text
2022-11-09 16:37:24.379549
```

```python
help('modules')
```

Recorded output:
```text

Please wait a moment while I gather a list of all available modules...
```

Recorded output:
```text
/usr/local/lib/python3.7/dist-packages/IPython/kernel/__init__.py:13: ShimWarning: The `IPython.kernel` package has been deprecated since IPython 4.0.You should import from ipykernel or jupyter_client instead.
  "You should import from ipykernel or jupyter_client instead.", ShimWarning)
/usr/local/lib/python3.7/dist-packages/llvmlite/llvmpy/__init__.py:4: UserWarning: The module `llvmlite.llvmpy` is deprecated and will be removed in the future.
  "The module `llvmlite.llvmpy` is deprecated and will be removed in the "
/usr/local/lib/python3.7/dist-packages/llvmlite/llvmpy/core.py:9: UserWarning: The module `llvmlite.llvmpy.core` is deprecated and will be removed in the future. Equivalent functionality is provided by `llvmlite.ir`.
  "The module `llvmlite.llvmpy.core` is deprecated and will be removed in "
WARNING: AstropyDeprecationWarning: The private astropy._erfa module has been made into its own package, pyerfa, which is a dependency of astropy and can be imported directly using "import erfa" [astropy._erfa]
WARNING:astropy:AstropyDeprecationWarning: The private astropy._erfa module has been made into its own package, pyerfa, which is a dependency of astropy and can be imported directly using "import erfa"
/usr/local/lib/python3.7/dist-packages/caffe2/__init__.py:5: UserWarning: Caffe2 support is not fully enabled in this PyTorch build. Please enable Caffe2 by building PyTorch from source with `BUILD_CAFFE2=1` flag.
  warnings.warn("Caffe2 support is not fully enabled in this PyTorch build. "
/usr/local/lib/python3.7/dist-packages/caffe2/proto/__init__.py:17: UserWarning: Caffe2 support is not enabled in this PyTorch build. Please enable Caffe2 by building PyTorch from source with `BUILD_CAFFE2=1` flag.
  warnings.warn('Caffe2 support is not enabled in this PyTorch build. '
/usr/local/lib/python3.7/dist-packages/caffe2/proto/__init__.py:17: UserWarning: Caffe2 support is not enabled in this PyTorch build. Please enable Caffe2 by building PyTorch from source with `BUILD_CAFFE2=1` flag.
  warnings.warn('Caffe2 support is not enabled in this PyTorch build. '
/usr/local/lib/python3.7/dist-packages/caffe2/python/__init__.py:9: UserWarning: Caffe2 support is not enabled in this PyTorch build. Please enable Caffe2 by building PyTorch from source with `BUILD_CAFFE2=1` flag.
  warnings.warn('Caffe2 support is not enabled in this PyTorch build. '
/usr/local/lib/python3.7/dist-packages/past/types/oldstr.py:5: DeprecationWarning:

Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3,and in 3.9 it will stop working

/usr/local/lib/python3.7/dist-packages/intervaltree/intervaltree.py:37: DeprecationWarning:

Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3,and in 3.9 it will stop working

/usr/local/lib/python3.7/dist-packages/jupyter_client/ssh/tunnel.py:57: DeprecationWarning:

zmq.utils.strtypes is deprecated in pyzmq 23.

/usr/local/lib/python3.7/dist-packages/librosa/core/constantq.py:1059: DeprecationWarning:

`np.complex` is a deprecated alias for the builtin `complex`. To silence this warning, use `complex` by itself. Doing this will not modify any behavior and is safe. If you specifically wanted the numpy scalar type, use `np.complex128` here.
Deprecated in NumPy 1.20; for more details and guidance: https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations
```

Recorded output:
```text
Downloading http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 to /root/mlxtend_data/shape_predictor_68_face_landmarks.dat.bz2
```

Recorded output:
```text
/usr/local/lib/python3.7/dist-packages/nbconvert/filters/strings.py:22: DeprecationWarning:

defusedxml.cElementTree is deprecated, import from defusedxml.ElementTree instead.

/usr/local/lib/python3.7/dist-packages/nibabel/quaternions.py:31: DeprecationWarning:

`np.float` is a deprecated alias for the builtin `float`. To silence this warning, use `float` by itself. Doing this will not modify any behavior and is safe. If you specifically wanted the numpy scalar type, use `np.float64` here.
Deprecated in NumPy 1.20; for more details and guidance: https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations

/usr/lib/python3.7/pkgutil.py:92: UserWarning:

The DICOM readers are highly experimental, unstable, and only work for Siemens time-series at the moment
Please use with caution.  We would be grateful for your help in improving them

/usr/local/lib/python3.7/dist-packages/nltk/twitter/__init__.py:21: UserWarning:

The twython library has not been installed. Some functionality from the twitter package will not be available.

/usr/local/lib/python3.7/dist-packages/pip/_vendor/packaging/version.py:130: DeprecationWarning:

Creating a LegacyVersion has been deprecated and will be removed in the next major release

/usr/local/lib/python3.7/dist-packages/pip/_vendor/packaging/version.py:130: DeprecationWarning:

Creating a LegacyVersion has been deprecated and will be removed in the next major release

/usr/lib/python3.7/pkgutil.py:92: UserWarning: Viewer requires Qt
/usr/local/lib/python3.7/dist-packages/sphinx/websupport/__init__.py:25: RemovedInSphinx20Warning: sphinx.websupport module is now provided as sphinxcontrib-websupport. sphinx.websupport will be removed at Sphinx-2.0. Please use the package instead.
/usr/local/lib/python3.7/dist-packages/marshmallow/fields.py:573: RemovedInMarshmallow4Warning: The 'missing' argument to fields is deprecated. Use 'load_default' instead.
/usr/local/lib/python3.7/dist-packages/tensorboard/_vendor/html5lib/filters/sanitizer.py:29: DeprecationWarning: html5lib's sanitizer is deprecated; see https://github.com/html5lib/html5lib-python/issues/443 and please let us know if Bleach is unsuitable for your needs
/usr/local/lib/python3.7/dist-packages/torch/distributed/_sharded_tensor/__init__.py:10: DeprecationWarning: torch.distributed._sharded_tensor will be deprecated, use torch.distributed._shard.sharded_tensor instead
/usr/local/lib/python3.7/dist-packages/torch/distributed/_sharding_spec/__init__.py:10: DeprecationWarning: torch.distributed._sharding_spec will be deprecated, use torch.distributed._shard.sharding_spec instead
```

Recorded output:
```text
No CUDA runtime is found, using CUDA_HOME='/usr/local/cuda'
```

Recorded output:
```text
/usr/lib/python3.7/pkgutil.py:107: VisibleDeprecationWarning: zmq.eventloop.minitornado is deprecated in pyzmq 14.0 and will be removed.
    Install tornado itself to use zmq with the tornado IOLoop.
```

Recorded output:
```text
Cython              collections         kaggle              requests
IPython             colorcet            kanren              requests_oauthlib
OpenGL              colorlover          kapre               resampy
PIL                 colorsys            keras               resource
ScreenResolution    community           keras_preprocessing rlcompleter
__future__          compileall          keyword             rmagic
_abc                concurrent          kiwisolver          rpy2
_ast                confection          korean_lunar_calendar rsa
_asyncio            configparser        langcodes           runpy
_bisect             cons                lib2to3             samples
_blake2             contextlib          libfuturize         sched
_bootlocale         contextlib2         libpasteurize       scipy
_bz2                contextvars         librosa             scs
_cffi_backend       convertdate         lightgbm            seaborn
_codecs             copy                linecache           secrets
_codecs_cn          copyreg             llvmlite            select
_codecs_hk          crashtest           lmdb                selectors
_codecs_iso2022     crcmod              locale              send2trash
_codecs_jp          crypt               locket              setuptools
_codecs_kr          csimdjson           logging             setuptools_git
_codecs_tw          csv                 lsb_release         shapely
_collections        ctypes              lunarcalendar       shelve
_collections_abc    cufflinks           lxml                shlex
_compat_pickle      curses              lzma                shutil
_compression        cv2                 macpath             signal
_contextvars        cvxopt              mailbox             simdjson
_crypt              cvxpy               mailcap             site
_csv                cycler              markdown            sitecustomize
_ctypes             cymem               markupsafe          six
_ctypes_test        cython              marshal             skimage
_curses             cythonmagic         marshmallow         sklearn
_curses_panel       daft                math                sklearn_pandas
_cvxcore            dask                matplotlib          slugify
_datetime           dataclasses         matplotlib_venn     smart_open
_dbm                datascience         mimetypes           smtpd
_decimal            datetime            missingno           smtplib
_distutils_hack     dateutil            mistune             sndhdr
_dlib_pybind11      dbm                 mizani              snowballstemmer
_dummy_thread       dbus                mlxtend             socket
_ecos               debugpy             mmap                socketserver
_elementtree        decimal             modulefinder        socks
_functools          decorator           more_itertools      sockshandler
_hashlib            defusedxml          moviepy             softwareproperties
_heapq              descartes           mpmath              sortedcontainers
_imp                difflib             msgpack             soundfile
_io                 dill                multidict           spacy
_json               dis                 multipledispatch    spacy_legacy
_locale             distributed         multiprocessing     spacy_loggers
_lsprof             distutils           multitasking        sphinx
_lzma               dlib                murmurhash          spwd
_markupbase         dns                 music21             sql
_md5                docs                natsort             sqlalchemy
_multibytecodec     doctest             nbconvert           sqlite3
_multiprocessing    docutils            nbformat            sqlparse
_opcode             dopamine            netCDF4             sre_compile
_operator           dot_parser          netrc               sre_constants
_osx_support        dummy_threading     networkx            sre_parse
_pickle             easydict            nibabel             srsly
_plotly_future_     ecos                nis                 ssl
_plotly_utils       editdistance        nisext              stan
_posixsubprocess    ee                  nltk                stat
_py_abc             email               nntplib             statistics
_pydecimal          en_core_web_sm      notebook            statsmodels
_pyio               encodings           ntpath              storemagic
_pyrsistent_version entrypoints         nturl2path          string
_pytest             enum                numba               stringprep
_queue              ephem               numbergen           struct
_random             erfa                numbers             subprocess
_rinterface_cffi_abi errno               numexpr             sunau
_rinterface_cffi_api et_xmlfile          numpy               symbol
_scs_direct         etils               oauth2client        sympy
_scs_indirect       etuples             oauthlib            sympyprinting
_sha1               fa2                 ogr                 symtable
_sha256             fastai              okgrade             sys
_sha3               fastcore            opcode              sysconfig
_sha512             fastdownload        openpyxl            syslog
_signal             fastdtw             operator            tables
_sitebuiltins       fastjsonschema      opt_einsum          tabnanny
_socket             fastprogress        optparse            tabulate
_soundfile          fastrlock           os                  tarfile
_sqlite3            faulthandler        osgeo               tblib
_sre                fcntl               osqp                telnetlib
_ssl                feather             osqppurepy          tempfile
_stat               filecmp             osr                 tenacity
_string             fileinput           ossaudiodev         tensorboard
_strptime           filelock            packaging           tensorboard_data_server
_struct             firebase_admin      palettable          tensorboard_plugin_wit
_symtable           fix_yahoo_finance   pandas              tensorflow
_sysconfigdata_m_linux_x86_64-linux-gnu flask               pandas_datareader   tensorflow_datasets
_sysconfigdata_m_x86_64-linux-gnu flatbuffers         pandas_gbq          tensorflow_estimator
_testbuffer         fnmatch             pandas_profiling    tensorflow_gcs_config
_testcapi           folium              pandocfilters       tensorflow_hub
_testimportmultiple formatter           panel               tensorflow_io_gcs_filesystem
_testmultiphase     fractions           param               tensorflow_metadata
_thread             frozenlist          parser              tensorflow_probability
_threading_local    fsspec              parso               termcolor
_tkinter            ftplib              partd               terminado
_tracemalloc        functools           past                termios
_warnings           future              pasta               test
_weakref            gast                pastel              testpath
_weakrefset         gc                  pathlib             tests
_xxtestfuzz         gdal                pathy               text_unidecode
_yaml               gdalconst           patsy               textblob
abc                 gdalnumeric         pdb                 textwrap
absl                gdown               pep517              thinc
aeppl               genericpath         pexpect             this
aesara              gensim              pickle              threading
aifc                geographiclib       pickleshare         threadpoolctl
aiohttp             geopy               pickletools         tifffile
aiosignal           getopt              pip                 time
alabaster           getpass             pipes               timeit
albumentations      gettext             piptools            tkinter
altair              gi                  pkg_resources       tlz
antigravity         gin                 pkgutil             token
apiclient           glob                platform            tokenize
appdirs             glob2               plistlib            toml
apt                 gnm                 plotly              tomli
apt_inst            google_auth_httplib2 plotlywidget        toolz
apt_pkg             google_auth_oauthlib plotnine            torch
aptsources          google_drive_downloader pluggy              torchaudio
argparse            googleapiclient     pooch               torchgen
array               googlesearch        poplib              torchsummary
arviz               graphviz            portpicker          torchtext
ast                 greenlet            posix               torchvision
astor               gridfs              posixpath           tornado
astropy             grp                 pprint              tqdm
astunparse          grpc                prefetch_generator  trace
async_timeout       gspread             preshed             traceback
asynchat            gspread_dataframe   prettytable         tracemalloc
asyncio             gym                 profile             traitlets
asyncore            gym_notices         progressbar         tree
asynctest           gzip                prometheus_client   tty
atari_py            h5py                promise             turtle
atexit              hashlib             prompt_toolkit      tweepy
atomicwrites        heapdict            prophet             typeguard
attr                heapq               pstats              typer
attrs               hijri_converter     psutil              types
audioop             hmac                psycopg2            typing
audioread           holidays            pty                 typing_extensions
autograd            holoviews           ptyprocess          tzlocal
autoreload          html                pwd                 unicodedata
babel               html5lib            py                  unification
backcall            http                py_compile          unittest
base64              httpimport          pyarrow             uritemplate
bdb                 httplib2            pyasn1              urllib
bin                 httpstan            pyasn1_modules      urllib3
binascii            humanize            pyclbr              uu
binhex              hyperopt            pycocotools         uuid
bisect              idna                pycparser           vega_datasets
bleach              imageio             pyct                venv
blis                imagesize           pydantic            vis
bokeh               imaplib             pydata_google_auth  warnings
boost               imblearn            pydoc               wasabi
branca              imgaug              pydoc_data          wave
bs4                 imghdr              pydot               wcwidth
bson                imp                 pydot_ng            weakref
builtins            importlib           pydotplus           webargs
bz2                 importlib_metadata  pydrive             webbrowser
cProfile            importlib_resources pyemd               webencodings
cachecontrol        imutils             pyexpat             werkzeug
cached_property     inflect             pygments            wheel
cachetools          inspect             pygtkcompat         widgetsnbextension
caffe2              intervaltree        pylab               wordcloud
calendar            io                  pylev               wrapt
catalogue           ipaddress           pymc                wsgiref
certifi             ipykernel           pymeeus             xarray
cffi                ipykernel_launcher  pymongo             xarray_einstats
cftime              ipython_genutils    pymystem3           xdrlib
cgi                 ipywidgets          pyparsing           xgboost
cgitb               isympy              pyrsistent          xkit
chardet             itertools           pysndfile           xlrd
charset_normalizer  itsdangerous        pytest              xlwt
chunk               jax                 python_utils        xml
clang               jaxlib              pytz                xmlrpc
click               jieba               pyviz_comms         xxlimited
client              jinja2              pywt                xxsubtype
clikit              joblib              pyximport           yaml
cloudpickle         jpeg4py             qdldl               yarl
cmake               json                qudida              yellowbrick
cmath               jsonschema          queue               zict
cmd                 jupyter             quopri              zipapp
cmdstanpy           jupyter_client      random              zipfile
code                jupyter_console     re                  zipimport
codecs              jupyter_core        readline            zipp
codeop              jupyterlab_plotly   regex               zlib
colab               jupyterlab_widgets  reprlib             zmq

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".
```
