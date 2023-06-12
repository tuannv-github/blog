=====
Async
=====

.. code-block:: C++

    template< class Function, class... Args >
    [[nodiscard]] std::future<std::invoke_result_t<std::decay_t<Function>,
                                               std::decay_t<Args>...>>
        async( std::launch policy, Function&& f, Args&&... args );

