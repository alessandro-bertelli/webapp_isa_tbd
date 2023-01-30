--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1 (Ubuntu 15.1-1.pgdg20.04+1)
-- Dumped by pg_dump version 15.1 (Ubuntu 15.1-1.pgdg20.04+1)

-- Started on 2023-01-29 10:56:51 CET

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- TOC entry 3391 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 214 (class 1259 OID 16390)
-- Name: bevanda; Type: TABLE; Schema: public; Owner: alessandro
--

CREATE TABLE public.bevanda (
    nome text NOT NULL,
    codice_bevanda integer NOT NULL,
    prezzo real NOT NULL
);


ALTER TABLE public.bevanda OWNER TO alessandro;

--
-- TOC entry 215 (class 1259 OID 16395)
-- Name: cliente; Type: TABLE; Schema: public; Owner: alessandro
--

CREATE TABLE public.cliente (
    nome text NOT NULL,
    telefono character varying,
    idcliente integer NOT NULL
);


ALTER TABLE public.cliente OWNER TO alessandro;

--
-- TOC entry 223 (class 1259 OID 32878)
-- Name: cliente_idcliente_seq; Type: SEQUENCE; Schema: public; Owner: alessandro
--

ALTER TABLE public.cliente ALTER COLUMN idcliente ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.cliente_idcliente_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 216 (class 1259 OID 16400)
-- Name: coupon; Type: TABLE; Schema: public; Owner: alessandro
--

CREATE TABLE public.coupon (
    codice_sconto character varying NOT NULL,
    valore integer NOT NULL
);


ALTER TABLE public.coupon OWNER TO alessandro;

--
-- TOC entry 217 (class 1259 OID 16405)
-- Name: ingred_pizza; Type: TABLE; Schema: public; Owner: alessandro
--

CREATE TABLE public.ingred_pizza (
    ingrediente text NOT NULL,
    codice_pizza integer NOT NULL
);


ALTER TABLE public.ingred_pizza OWNER TO alessandro;

--
-- TOC entry 218 (class 1259 OID 16410)
-- Name: ordine_bevanda; Type: TABLE; Schema: public; Owner: alessandro
--

CREATE TABLE public.ordine_bevanda (
    n_pezzi integer NOT NULL,
    id_prenotazione integer NOT NULL,
    codice_bevanda integer NOT NULL
);


ALTER TABLE public.ordine_bevanda OWNER TO alessandro;

--
-- TOC entry 219 (class 1259 OID 16415)
-- Name: ordine_pizza; Type: TABLE; Schema: public; Owner: alessandro
--

CREATE TABLE public.ordine_pizza (
    n_pezzi integer NOT NULL,
    id_prenotazione integer NOT NULL,
    codice_pizza integer NOT NULL
);


ALTER TABLE public.ordine_pizza OWNER TO alessandro;

--
-- TOC entry 220 (class 1259 OID 16420)
-- Name: pizza; Type: TABLE; Schema: public; Owner: alessandro
--

CREATE TABLE public.pizza (
    nome text NOT NULL,
    codice_pizza integer NOT NULL,
    prezzo double precision NOT NULL
);


ALTER TABLE public.pizza OWNER TO alessandro;

--
-- TOC entry 221 (class 1259 OID 16425)
-- Name: prenotazione; Type: TABLE; Schema: public; Owner: alessandro
--

CREATE TABLE public.prenotazione (
    id_prenotazione integer NOT NULL,
    data date NOT NULL,
    orario time without time zone NOT NULL,
    idcliente integer NOT NULL
);


ALTER TABLE public.prenotazione OWNER TO alessandro;

--
-- TOC entry 222 (class 1259 OID 24757)
-- Name: prenotazione_id_prenotazione_seq; Type: SEQUENCE; Schema: public; Owner: alessandro
--

ALTER TABLE public.prenotazione ALTER COLUMN id_prenotazione ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.prenotazione_id_prenotazione_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 3376 (class 0 OID 16390)
-- Dependencies: 214
-- Data for Name: bevanda; Type: TABLE DATA; Schema: public; Owner: alessandro
--

COPY public.bevanda (nome, codice_bevanda, prezzo) FROM stdin;
"Acqua Naturale Bottiglia di Vetro"	1	2.6
"Acqua Frizzante Bottiglia di Vetro"	2	2.6
"Coca-cola in Bottiglia di Vetro 33cl"	3	3
"Fanta  in Bottiglia di Vetro 33cl"	4	3
"Sprite  in Bottiglia di Vetro 33cl"	5	3
"Tè al Limone  in Bottiglia di Vetro 33cl"	6	3
"N'Artigiana Oro 33cl"	8	4.5
"N'Artigiana Doppio Malto 33cl"	9	4.7
"San Biagio Monasta Ambrata 75 cl"	10	6
"Tè alla Pesca in Bottiglia di Vetro 33cl"	7	3
\.


--
-- TOC entry 3377 (class 0 OID 16395)
-- Dependencies: 215
-- Data for Name: cliente; Type: TABLE DATA; Schema: public; Owner: alessandro
--

COPY public.cliente (nome, telefono, idcliente) FROM stdin;
test_name	1234567890	87
\.


--
-- TOC entry 3378 (class 0 OID 16400)
-- Dependencies: 216
-- Data for Name: coupon; Type: TABLE DATA; Schema: public; Owner: alessandro
--

COPY public.coupon (codice_sconto, valore) FROM stdin;
3461579	10
3461589	10
7346898	15
5846523	5
2565854	5
6974541	5
5265856	5
3985463	10
\.


--
-- TOC entry 3379 (class 0 OID 16405)
-- Dependencies: 217
-- Data for Name: ingred_pizza; Type: TABLE DATA; Schema: public; Owner: alessandro
--

COPY public.ingred_pizza (ingrediente, codice_pizza) FROM stdin;
"Pomodoro San Marzano pelato"	1
"Olio extravergine d'oliva"	1
"Origano"	1
"Aglio"	1
"Basilico fresco"	1
"Pomodoro San Marzano pelato"	2
"Olio extravergine d'oliva"	2
"Origano"	2
"Aglio"	2
"Basilico fresco"	2
"Filetto di pomodoro"	3
"Mozzarella fiordilatte di Agerola"	3
"Olio extravergine di oliva"	3
"Basilico fresco"	3
"Salsiccia di maialino nero Casertano"	4
"Friarielli"	4
"Provola di Agerola"	4
"Grana Padano"	4
"Ricotta fresca"	5
"Provole di Agerola"	5
"Salame Irpino"	5
"Pomodoro San Marzano pelato"	5
"Pepe"	5
"Basilico fresco"	5
"Olio extravergine di oliva"	5
"Ricotta fresca"	6
"Provola di Agerola"	6
"Cicoli"	6
"Pepe"	6
"Gorgonzola fresco"	7
"Panna"	7
"Emmental"	7
"Mozzarella fiordilatte di Agerola"	7
"Basilico fresco"	7
"Grana Padano"	7
"Olio Extra Vergine d'oliva"	7
"Pomodoro San Marzano"	8
"Salame Irpino"	8
"Peperoncino macinato"	8
"Mozzarella fiordilatte"	8
"Grana padano"	8
"Basilico fresco"	8
"Olio extra vergine d'oliva"	8
\.


--
-- TOC entry 3380 (class 0 OID 16410)
-- Dependencies: 218
-- Data for Name: ordine_bevanda; Type: TABLE DATA; Schema: public; Owner: alessandro
--

COPY public.ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda) FROM stdin;
\.


--
-- TOC entry 3381 (class 0 OID 16415)
-- Dependencies: 219
-- Data for Name: ordine_pizza; Type: TABLE DATA; Schema: public; Owner: alessandro
--

COPY public.ordine_pizza (n_pezzi, id_prenotazione, codice_pizza) FROM stdin;
\.


--
-- TOC entry 3382 (class 0 OID 16420)
-- Dependencies: 220
-- Data for Name: pizza; Type: TABLE DATA; Schema: public; Owner: alessandro
--

COPY public.pizza (nome, codice_pizza, prezzo) FROM stdin;
"Marinara"	1	6
"Margherita"	2	7
"Fileto"	3	8.5
"Salsiccia e Friarielli"	4	11
"Ripieno al forno"	5	11
"Ripieno fritto"	6	11
"4 formaggi"	7	10
"Diavola"	8	8.5
\.


--
-- TOC entry 3383 (class 0 OID 16425)
-- Dependencies: 221
-- Data for Name: prenotazione; Type: TABLE DATA; Schema: public; Owner: alessandro
--

COPY public.prenotazione (id_prenotazione, data, orario, idcliente) FROM stdin;
113	1111-11-11	00:00:00	87
\.


--
-- TOC entry 3392 (class 0 OID 0)
-- Dependencies: 223
-- Name: cliente_idcliente_seq; Type: SEQUENCE SET; Schema: public; Owner: alessandro
--

SELECT pg_catalog.setval('public.cliente_idcliente_seq', 87, true);


--
-- TOC entry 3393 (class 0 OID 0)
-- Dependencies: 222
-- Name: prenotazione_id_prenotazione_seq; Type: SEQUENCE SET; Schema: public; Owner: alessandro
--

SELECT pg_catalog.setval('public.prenotazione_id_prenotazione_seq', 113, true);


--
-- TOC entry 3213 (class 2606 OID 16431)
-- Name: bevanda bevanda_pk; Type: CONSTRAINT; Schema: public; Owner: alessandro
--

ALTER TABLE ONLY public.bevanda
    ADD CONSTRAINT bevanda_pk PRIMARY KEY (codice_bevanda);


--
-- TOC entry 3215 (class 2606 OID 32872)
-- Name: cliente cliente_pk; Type: CONSTRAINT; Schema: public; Owner: alessandro
--

ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_pk PRIMARY KEY (idcliente);


--
-- TOC entry 3217 (class 2606 OID 16435)
-- Name: coupon coupon_pk; Type: CONSTRAINT; Schema: public; Owner: alessandro
--

ALTER TABLE ONLY public.coupon
    ADD CONSTRAINT coupon_pk PRIMARY KEY (codice_sconto);


--
-- TOC entry 3219 (class 2606 OID 16437)
-- Name: ingred_pizza ingred_pizza_pk; Type: CONSTRAINT; Schema: public; Owner: alessandro
--

ALTER TABLE ONLY public.ingred_pizza
    ADD CONSTRAINT ingred_pizza_pk PRIMARY KEY (ingrediente, codice_pizza);


--
-- TOC entry 3221 (class 2606 OID 24731)
-- Name: ordine_bevanda ordine_bevanda_pk; Type: CONSTRAINT; Schema: public; Owner: alessandro
--

ALTER TABLE ONLY public.ordine_bevanda
    ADD CONSTRAINT ordine_bevanda_pk PRIMARY KEY (id_prenotazione, codice_bevanda);


--
-- TOC entry 3223 (class 2606 OID 24742)
-- Name: ordine_pizza ordine_pizza_pk; Type: CONSTRAINT; Schema: public; Owner: alessandro
--

ALTER TABLE ONLY public.ordine_pizza
    ADD CONSTRAINT ordine_pizza_pk PRIMARY KEY (id_prenotazione, codice_pizza);


--
-- TOC entry 3225 (class 2606 OID 16443)
-- Name: pizza pizza_pk; Type: CONSTRAINT; Schema: public; Owner: alessandro
--

ALTER TABLE ONLY public.pizza
    ADD CONSTRAINT pizza_pk PRIMARY KEY (codice_pizza);


--
-- TOC entry 3227 (class 2606 OID 24723)
-- Name: prenotazione prenotazione_pk; Type: CONSTRAINT; Schema: public; Owner: alessandro
--

ALTER TABLE ONLY public.prenotazione
    ADD CONSTRAINT prenotazione_pk PRIMARY KEY (id_prenotazione);


--
-- TOC entry 3228 (class 2606 OID 16451)
-- Name: ingred_pizza ingred_pizza_fk; Type: FK CONSTRAINT; Schema: public; Owner: alessandro
--

ALTER TABLE ONLY public.ingred_pizza
    ADD CONSTRAINT ingred_pizza_fk FOREIGN KEY (codice_pizza) REFERENCES public.pizza(codice_pizza);


--
-- TOC entry 3229 (class 2606 OID 24736)
-- Name: ordine_bevanda ordine_bevanda_fk; Type: FK CONSTRAINT; Schema: public; Owner: alessandro
--

ALTER TABLE ONLY public.ordine_bevanda
    ADD CONSTRAINT ordine_bevanda_fk FOREIGN KEY (id_prenotazione) REFERENCES public.prenotazione(id_prenotazione);


--
-- TOC entry 3230 (class 2606 OID 16461)
-- Name: ordine_bevanda ordine_bevanda_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: alessandro
--

ALTER TABLE ONLY public.ordine_bevanda
    ADD CONSTRAINT ordine_bevanda_fk_1 FOREIGN KEY (codice_bevanda) REFERENCES public.bevanda(codice_bevanda);


--
-- TOC entry 3231 (class 2606 OID 24747)
-- Name: ordine_pizza ordine_pizza_fk; Type: FK CONSTRAINT; Schema: public; Owner: alessandro
--

ALTER TABLE ONLY public.ordine_pizza
    ADD CONSTRAINT ordine_pizza_fk FOREIGN KEY (id_prenotazione) REFERENCES public.prenotazione(id_prenotazione);


--
-- TOC entry 3232 (class 2606 OID 16471)
-- Name: ordine_pizza ordine_pizza_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: alessandro
--

ALTER TABLE ONLY public.ordine_pizza
    ADD CONSTRAINT ordine_pizza_fk_1 FOREIGN KEY (codice_pizza) REFERENCES public.pizza(codice_pizza);


--
-- TOC entry 3233 (class 2606 OID 32873)
-- Name: prenotazione prenotazione_fk; Type: FK CONSTRAINT; Schema: public; Owner: alessandro
--

ALTER TABLE ONLY public.prenotazione
    ADD CONSTRAINT prenotazione_fk FOREIGN KEY (idcliente) REFERENCES public.cliente(idcliente);


-- Completed on 2023-01-29 10:56:51 CET

--
-- PostgreSQL database dump complete
--

