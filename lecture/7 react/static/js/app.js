'use strict';

// import { newsList } from "./chinews";

// const Link = ReactRouterDOM.Link;
// const Route = ReactRouterDOM.Route;

const List = () => {
  const [newsList, setNewsList] = React.useState([]);
  // const [loading, setLoading] = ReactDOMuseState(true);
  // const [error, setError] = ReactDOMuseState(null);
 
  React.useEffect(() => {
   fetch(`api/list?offset=0`)
    .then((response) => {
      console.log(response)
      return response.json()
    }).then((data) => {
      setNewsList(data)
    })
  }, []);

    return (
      <>
        <ul>
          {newsList.map((data, key) => {
            return (
              <li key={key}>
                <h3>
                <Link to={`page/${key}`}>{data.ru_title}</Link>
                </h3>
              </li>
            );
          })}
        </ul>
      </>
    );
  };


  const News = () => {
    let { id } = ReactRouterDOM.useParams();
    const [news, setNews] = React.useState([]);

    React.useEffect(() => {
      fetch(`/api/page/${id}`)
       .then((response) => {
         console.log(response)
         return response.json()
       }).then((data) => {
         setNews(data)
       })
     }, []);

    return (
      <>
        <p>
            Дата: <i>{news.date}</i>
        </p>
        <h2>
        {news.ru_title}
        </h2>


        <p size="20">
        {news.ru_desc}
        </p>

        <dl>
            <dt>источник</dt>
            <dd>
                <a href={news.url}>{news.source}</a>
            </dd>
        </dl>
      </>
    )
  }

  const Link = ReactRouterDOM.Link;
  const Route = ReactRouterDOM.Route;


const App = () => (
  <ReactRouterDOM.BrowserRouter>
    {/* <ul>
      <li><Link to="/">Home</Link></li>
      <li><Link to="/page">Login</Link></li>
    </ul> */}

    <Route path="/" exact component={List} />
    <Route path="/page/:id">
      <News />
    </Route>
  </ReactRouterDOM.BrowserRouter>
)

const rootNode = document.getElementById('root');
const root = ReactDOM.createRoot(rootNode);
root.render(<App />);
