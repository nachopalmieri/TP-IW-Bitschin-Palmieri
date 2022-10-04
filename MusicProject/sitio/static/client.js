
class Client {
    #api

    constructor() {
        this.#api = axios.create({
            baseURL: '/api',
            timeout: 5000,
            withCredentials: true,
        });
    }

    #url(path) {
        return path.replace('/api', '');
    }

    get(path, { params = null } = {}) {
        return this.#api.get(this.#url(path), params ? { params } : {});
    }

    getPublications(page = 1) {
        return this.get('/publications', { params: { page } })
            .then((response) => {
                return response.data.results;
            });
    }

}

const client = new Client();

export { client };